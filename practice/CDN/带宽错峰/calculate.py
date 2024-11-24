import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Microsoft YaHei')


def cal(df):
    return df[df != 0].quantile(0.95)


def bandwidth(servers,path1,path2,path3,path4):
    temp_data_0={}
    temp_data_3={}
    for server in servers:
        temp_data_0[server.ID] = server.bandwidth_monitor
        temp_data_3[server.ID] = server.bandwidth_level

    df_bandwidth_unsorted = pd.DataFrame(temp_data_0)[288:-288]
    #将df_bandwidth_unsorted按照每列的大小各自进行从大到小排序
    df_bandwidth = df_bandwidth_unsorted.apply(lambda x: x.sort_values(ascending=False).values)
    df_bandwidth_level = pd.DataFrame(temp_data_3)
    # 将非常接近零的值替换为零
    threshold = 1e-5  # 设置一个阈值，小于该值的数据将被替换为零
    df_bandwidth[df_bandwidth.abs() < threshold] = 0
    df_bandwidth_unsorted[df_bandwidth_unsorted.abs() < threshold] = 0
    df_bandwidth_level[df_bandwidth_level.abs() < threshold] = 0
    df_95 = df_bandwidth.apply(cal,axis=0)
    cost = {}  # 用于存储成本值
    for value, server in zip(df_95, servers):
        cost[server.ID] = value * server.cost
    df_cost = pd.DataFrame(cost,index=[0])
    # df_cost.to_excel(path1,index=False,engine='openpyxl')
    # df_bandwidth.to_excel(path2,index=False)
    # df_bandwidth_unsorted.to_excel(path3,index=False)
    # df_bandwidth_level.to_excel(path4,index=False)
    return df_cost.sum(axis=1)

def check(servers,users):
    count_all = 0
    count = []
    for server in servers:
        if server.level == 2:
            count_all += server.serverd_count
    for user in users:
        if user.status == False:
            count.append(user.ID)
    print(f"总共服务{count_all}次")
    print(f'没有被服务的客户ID{count}')    


def cal_wait(users, path5):
    # 创建一个空字典来存储用户等待时间
    wait = {}   
    for user in users:
        if user.wait_time != 0:
            wait[user.ID] = user.wait_time
    df_wait = pd.DataFrame(wait,index=[0]) 
    df_wait.to_excel(path5,index=False,engine='openpyxl')

def draw_bandwidth(servers,time):
    temp_data_0={}
    temp_data_0['time'] =  np.arange(0, time, 5)
    for server in servers:
        temp_data_0[server.ID] = server.bandwidth_monitor

    df_bandwidth = pd.DataFrame(temp_data_0)
    df_bandwidth = df_bandwidth.set_index('time')

    row_sums = df_bandwidth.sum(axis=1)
    # 将非常接近零的值替换为零
    threshold = 1e-5  # 设置一个阈值，小于该值的数据将被替换为零
    df_bandwidth[df_bandwidth.abs() < threshold] = 0
    # 创建图形对象
    fig, ax = plt.subplots(figsize=(12, 6))
    # 绘制time和row_sums的折线图
    plt.plot(df_bandwidth.index, row_sums)
    # 设置图表标题和标签
    plt.title('带宽变化图')
    plt.xticks(range(0, time, 60), range(1, (time//60)+1))
    plt.ylabel('带宽')
    plt.xlabel('时间')
    plt.show()
