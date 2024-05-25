import pandas as pd
import simpy

# 获得当前仿真时间
def get_current_timestamp(env, base_date="06:00:00"):
    simulation_time = env.now
    return (pd.Timestamp(base_date) + pd.Timedelta(seconds=simulation_time)).time()


