n = int(input())
heights = [int(input()) for _ in range(n)]
# j=0 表示最后一步是爬升，j=1 表示最后一步是跳跃
dp = [[0, 0] for _ in range(n+1)]
# 起始点不管是爬升还是跳跃都是0
dp[0][0],dp[0][1] = 0,0
for i in range(1,n+1):
    # 该层爬升，上一层爬升或者跳跃,爬的时间在于前两层跳的时间最小的加上该层数层高
    dp[i][0] = min(dp[i-1][0]+heights[i-1],dp[i-1][1]+heights[i-1])
    # 该层跳跃，上一次操作跳一步或者两步
    dp[i][1] = min(dp[i-1][0],dp[i-2][0])
print(min(dp[-1][0],dp[-1][1]))

