roads = [[0,1],[0,2],[0,3]]
seats = 5
def minimumFuelCost(roads,seats):
    def dfs(city):
        p = 1
        for neighbor in t



    g = [[] for _ in range(len(roads) + 1)]
    print(g)
    for (x, y) in roads:
        g[x].append(y)  # 记录每个点的邻居
        g[y].append(x)
        print(g)
    visited = [False]*n
    visited[0]=True
    ans = 0



minimumFuelCost(roads, seats)