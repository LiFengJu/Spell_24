import pandas as pd
def describe_missing(df, ascending=True):
    """
    描述DataFrame中的缺失值情况。

    参数：
        df (pd.DataFrame)：输入的DataFrame。
        ascending (bool, 可选)：如果为True，则按升序排列；否则按降序排列。
            默认为False（降序）。

    返回：
        pd.DataFrame：包含有关缺失值信息的DataFrame，包括数量、百分比和类型。

    示例：
        result_descending = describe_missing(df)
        result_ascending = describe_missing(df, ascending=True)
    """
    # 计算每列缺失值的数量，按指定顺序排序
    missing_info = (
        df.isnull().sum().sort_values(ascending=ascending)
        .loc[lambda x: x > 0]
        .to_frame(name='Missing')
        .assign(Percentage=lambda x: x / df.shape[0])
        .join(df.dtypes.to_frame(name='Type'))
        .rename(columns={'Percentage': 'Percentage', 'Missing': 'Missing', 'Type': 'Type'})
    )
    return missing_info

def draw_picture(df,y):
    numeric_columns = df.select_dtypes(include=['number'])
    categorical_columns = df.select_dtypes(include = 'O')
    numeric_columns.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
    sns.pairplot(df,x_vars=numeric_columns.columns,y_vars=y)
    numeric_columns = df.select_dtypes(include=['number'])
    corrmat = numeric_columns.corr()
    sns.heatmap(corrmat, annot=True, fmt='.2f', vmax=.8, annot_kws={'size': 5}, square=True)