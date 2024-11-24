# 读取输入
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# 初始化dp数组
dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

# 动态规划
for i in range(1, n + 1):
    for j in range(m + 1):
        # 不贴标签
        dp[i][j] = max(dp[i][j], dp[i - 1][j] + c[i - 1])
        # 贴标签
        if j > 0 and j == a[i - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + b[i - 1])

# 找到最大美观值
max_beauty = max(dp[n])
print(max_beauty)