import simpy
import pandas as pd
import request as re
import random
import numpy as np
import hashlib


# 定义服务器类
class Server:
    def __init__(self, env, ID, level ,balanced_bandwidth_limit, max_bandwidth,coordinate,cost):
        self.env = env
        self.ID = ID
        self.level = level
        self.balanced_bandwidth_limit = balanced_bandwidth_limit
        self.max_bandwidth = max_bandwidth
        self.gap = max_bandwidth - balanced_bandwidth_limit
        self.cost = cost
        self.resource = simpy.PriorityResource(
                        self.env,capacity=simpy.core.Infinity)
        self.bandwidth = simpy.Container(
                        self.env,init=balanced_bandwidth_limit)
        self.being_served_users = []
        self.users_waiting = []
        self.served_users = []
        self.serverd_count = 0  
        self.coordinate = coordinate
        self.service_flag = True  # 初始时允许服务新用户
        self.model = 0
        self.monitor = env.event()
        self.five_miniute = env.event()
        self.bandwidth_monitor = []
        self.bandwidth_level = []
        self.change = self.env.process(self.change_bandwidth_capacity())
        self.mon_proc = self.env.process(self.monitor_bandwidth())
        self.five = self.env.process(self.five_check())
        self.mon_wait = self.env.process(self.check_waiting_users())
        self.random_factor = random.randint(0, 10)
        self.go = False


    def change_bandwidth_capacity(self):
        while True:
            yield self.env.timeout(540)
            if self.model == 0:
                self.model = 1   
                self.increase_bandwidth()
            yield self.env.timeout(36)
            if self.model == 1:
             # 先禁止服务新用
                self.service_flag = False
                self.reduce_bandwidth()
            yield self.env.timeout(564)
            if self.model == 0:
                self.model = 1   
                self.increase_bandwidth()
            yield self.env.timeout(36)
            if self.model == 1:
             # 先禁止服务新用
                self.service_flag = False
                self.reduce_bandwidth()
            yield self.env.timeout(264)

    def increase_bandwidth(self):
        self.bandwidth.put(self.gap)

    def reduce_bandwidth(self):
        # 检查服务器的带宽资源是否大于应减带宽。
        if self.bandwidth.level >= (self.gap):
            self.bandwidth.get(self.gap)
            #更改带宽限制后，允许服务新用户
            self.service_flag = True
            self.model = 0

    def check_waiting_users(self):
        while True:
            if self.users_waiting:
                self.env.process(self.serve_waiting_users())
            yield self.env.timeout(0.1)

    def five_check(self):
        while True:
            self.go = True
            self.five_miniute.succeed()
            self.five_miniute = self.env.event()
            yield self.env.timeout(5)


    def monitor_bandwidth(self):
        while True:
            self.go = False
            period_bandwidth = [0]
            while True:
                yield  self.monitor | self.five_miniute
                if self.go == True:
                    break
                else:
                    if self.model == 0:
                        period_bandwidth.append(max((self.balanced_bandwidth_limit-self.bandwidth.level),0))
                    else:
                        period_bandwidth.append(max((self.max_bandwidth-self.bandwidth.level),0))
            self.bandwidth_level.append(self.bandwidth.level)
            self.bandwidth_monitor.append(np.max(period_bandwidth))

    def serve(self, user):
        if self.service_flag and user.served[self.level] == 0 and user.bandwidth_request <= self.bandwidth.level:
            # 将用户当前层级标记为已服务
            user.served[self.level] = 1
            # 计算用户的等待时间
            user.wait_time += self.env.now - user.start_wait
            # 将用户添加到正在被服务的用户列表中
            self.being_served_users.append(user)
            # 从服务器的带宽资源中申请带宽
            self.bandwidth.get(user.bandwidth_request)
            # 从带宽资源中申请带宽后，触发带宽监控事件
            self.monitor.succeed()
            self.monitor = self.env.event()
            # 等待服务结束
            yield self.env.timeout(user.service_time)
            # 释放带宽资源
            self.bandwidth.put(user.bandwidth_request)
            # 释放带宽资源后，触发带宽监控事件
            self.monitor.succeed()
            self.monitor = self.env.event()
            user.serve_over.succeed()
            user.serve_over = self.env.event()
            # 从正在被服务的用户列表中移除用户
            self.being_served_users.remove(user)
            # 增加服务器的已服务次数
            self.serverd_count += 1
            # 记录用户的服务情况
            self.served_users.append(user.ID)
            user.served_servers.append(self.ID)
            # 检查服务器是否允许服务新用户
            if self.service_flag == False:
                # 尝试将服务器的带宽资源减少到均衡带宽
                self.reduce_bandwidth()
                # 如果成功减少带宽，检查是否有用户在等待且服务器允许服务新用户
            if self.service_flag == True:   
                self.env.process(self.serve_waiting_users())
        # else:
        #     #打印错误日志
        #     print(f"User {user.ID} cannot be served.")

    def serve_waiting_users(self):
        # 如果有用户在等待且服务器允许服务新用户
        if self.users_waiting and self.service_flag:
            waiting_users = sorted((user for user in self.users_waiting if user.served[self.level] == 0),
                                key=lambda x: (x.priority, x.arrive_time))

            to_remove = []  # 待移除的用户列表
            for user in waiting_users:
                if user.bandwidth_request <= self.bandwidth.level:
                    # 从服务器的带宽资源中申请带宽，并开始服务
                    with self.resource.request(priority=user.priority) as req:
                        yield req   
                        yield self.env.process(self.serve(user))
                        to_remove.append(user)
                        break
            # 一次性移除要删除的用户
            self.users_waiting = [user for user in waiting_users if user not in to_remove]


# 用户类
class User:
    def __init__(self, env,data_amount, ID,level, bandwidth_request, priority, interval_time,coordinate,ip_addresses):
        self.env = env
        self.ID = ID
        self.bandwidth_request = bandwidth_request
        self.priority = priority
        self.arrive_time = 0
        self.interval_time = interval_time
        self.service_time = abs(data_amount/bandwidth_request + np.random.normal(10,2))
        self.served = [0,0,0]
        self.coordinate = coordinate
        self.level = level
        self.wait_time = 0
        self.near_servers = []
        self.start_wait = 0
        self.served_servers=[]
        self.status = False
        self.random_factor = random.randint(0, 50)
        self.ip_address = ip_addresses
        self.serve_over = env.event()

    def near_search(self,servers,key=None):
        distance={}
        # 计算用户与服务器的距离
        for server in servers:
            if server.level == self.level:
                distance[server] = (server.coordinate[0]-self.coordinate[0])**2+(server.coordinate[1]-self.coordinate[1])**2
        
        temp = [key for key, _ in sorted(distance.items(), key=lambda x: x[1])[:5]]
        self.near_servers = temp
        if self.level ==1 or 0:
            self.near_servers = temp[:1]
        else:
            if key == 'cost':
                self.near_servers.sort(key=lambda x: x.cost)
            elif key == 'least_connection':
                self.near_servers.sort(key=lambda x: len(x.being_served_users))
            elif key == 'ip_hash':
                self.near_servers = self.near_servers[self.ip_index():self.ip_index()+1]

    def random_one(self):
        arr=[]
        for server in self.near_servers:
            arr.append(server.random_factor)
        cumulative_sum = 0
        nearest_index = None
        min_difference = float('inf')  # 用于跟踪最小差异的初始值设定为正无穷大

        for i, value in enumerate(arr):
            cumulative_sum += value
            difference = abs(cumulative_sum - self.random_factor)

            if difference < min_difference:
                min_difference = difference
                nearest_index = i
        temp=[]
        temp.append(self.near_servers[nearest_index])
        return temp
    
    def ip_index(self):
        hash_value = int(hashlib.md5(self.ip_address.encode()).hexdigest(), 16)
        server_index = hash_value % 5
        return server_index


def creat_servers_excel(env,path1):
    # 读取服务器信息
    server_data =pd.read_excel(path1) 
    # 创建服务器列表
    servers = []
    # 遍历服务器信息并将其创建为 server 类的实例，然后添加到服务器列表中
    for _, row in server_data.iterrows():
        server = Server(
            env=env,
            ID=row['编号'],
            level=row['保存数据类型'],
            balanced_bandwidth_limit=row['平稳带宽'],
            max_bandwidth=row['最大带宽'],
            coordinate=(row['x'], row['y']),
            cost=row['带宽成本']
            # 添加其他服务器属性
        )
        servers.append(server)
    return servers

def creat_users_excel(env,user_data):
    users = []
    # 遍历用户信息并将其创建为 User 类的实例，然后添加到用户列表中
    for _, row in user_data.iterrows():
        user = User(
            env=env,
            ID=row['编号'],
            level=row['请求数据类型'],
            priority=row['优先级'],
            data_amount=row['数据量'],
            bandwidth_request=row['请求带宽'],
            interval_time=row['间隔时间'],
            coordinate=(row['x'], row['y']),
            ip_addresses=['IP地址']
            # 添加其他用户属性
        )
        users.append(user)
    return users


def gen_users_auto(env,i,x,y):
    user = User(
        env=env,
        ID=i,
        level=np.random.choice([0,1,2],p=[0.1,0.2,0.7]),
        priority=np.random.choice([0,1,2,3],p=[0.05,0.15,0.3,0.5]),
        data_amount=np.clip(np.random.gamma(1,70),0,5000),
        bandwidth_request=abs(np.random.normal(50,30)),
        interval_time=0,
        coordinate=(x, y),
        ip_addresses = generate_random_ipv4()
        # 添加其他用户属性  
    )
    return user


def arrive(env, user_data, servers, name, key,users): 
    if key == 'auto':
        X = user_data['x']
        Y = user_data['y']
        L = len(user_data)
        while True: 
            i = np.random.randint(0,L)
            x,y = X[i],Y[i]
            user = gen_users_auto(env,i,x,y)
            user.interval_time = generate_interval_time(env.now)
            yield env.timeout(user.interval_time)
            user.arrive_time = env.now
            env.process(re.request(user,servers,name))
            users.append(user)
    elif key == 'excel':
        users = creat_users_excel(env,user_data)
        for user in users:
            yield env.timeout(user.interval_time)
            user.arrive_time = env.now
            env.process(re.request(env,user,servers,name))
   


# 生成随机的IPv4地址
def generate_random_ipv4():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# 生成随机的时间间隔
def generate_interval_time(time_now):
    time_day = (time_now % 1440)/60
    lambda_value = generate_lambda(time_day)
    interval_time = np.round(np.random.exponential(1/lambda_value) + np.random.normal(0,0.001),5)*5
    interval_time = abs(interval_time)
    return interval_time

#根据一天不同的时间段生成不同的lambda, 表示单位时间内（一分钟）到达平均的用户数量
def generate_lambda(time_day):
    if time_day <= 1:
        return 80
    elif time_day <= 2:
        return 50
    elif time_day <= 3:
        return 30
    elif time_day <= 5:
        return 20
    elif time_day <= 7:
        return 50
    elif time_day <= 9:
        return 120
    elif time_day <= 12:
        return 200
    elif time_day <= 14:
        return 120
    elif time_day <= 17:
        return 170
    elif time_day <= 19:
        return 150
    elif time_day <= 21:
        return 200
    elif time_day <= 23:
        return 150
    elif time_day <= 24:
        return 120
