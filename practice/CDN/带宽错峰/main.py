import simpy
import class_data as cd
import calculate as cal
import pandas as pd
import numpy as np

cost = {}
for i in range(10):
    # 创建 SimPy 环境
    env = simpy.Environment()
    # 读取服务器信息
    key =   'auto' #input("form excel OR auto generate:")
    name ='near' #input("name:") 
    time = int('46080')     #input("time")
    servers = cd.creat_servers_excel(env,'服务器数据1.xlsx')
    
    
    user_data = pd.read_excel('客户数据1.xlsx')
    users = []
    env.process(cd.arrive(env, user_data,servers,name,key,users))
    env.process(cd.contral_bandwidth(servers))
    env.run(until=time)
    
    #输出结果
    c = cal.bandwidth(servers,f'{name}带宽成本{i}.xlsx',f'{name}排序带宽{i}.xlsx',f'{name}原始带宽.xlsx',f'{name}带宽余量.xlsx')
    cost[i] = c
    # cal.cal_wait(users, f'{name}等待时间{i}.xlsx')     
    cal.draw_bandwidth(servers,time)
    # cal.check(servers,users)
        
df_overall_cost = pd.DataFrame(cost)
df_overall_cost.to_excel('成本.xlsx',index=False,engine='openpyxl')
