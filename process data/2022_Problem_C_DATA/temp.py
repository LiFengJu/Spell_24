import pandas as pd

# 读取CSV文件
df = pd.read_csv('BCHAIN-MKPRU.csv')

# 添加一列用于存储解析后的日期
df['parsed_date'] = pd.to_datetime(df['date'], errors='coerce')

