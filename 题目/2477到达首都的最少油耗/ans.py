class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """
        * 对当前城市节点city进行深度优先搜索，返回去往首都路上经过该城市的代表人数
         @param city: 当前城市节点编号
         @param tree: 树结构，tree[i] 表示城市节点i的所有邻节点
         @param visited: 表示城市节点是否访问过
         @seats: 每辆车的容量
         @return：返回去往首都路上经过该城市的代表人数people
        """
        def dfs(city: int) -> int:
            people = 1     # 该城市本身有一个代表
            # 枚举当前城市节点的所有邻节点
            for neighbor in tree[city]:
                # 处理未遍历过的邻节点
                if not visited[neighbor]:
                    visited[neighbor] = True
                    people += dfs(neighbor)  # 累加到达当前城市的代表人数
            if city:
                # city不为0，就需要在移动到下一个节点，people个代表需要的车辆数等于people ÷ seats 向上取整
                # 即有这么多辆车从当前节点到达下一个节点，每辆车消耗1汽油
                self.fuel += (people + seats - 1) // seats
            return people

        self.fuel = 0
        n = len(roads) + 1       # 节点个数
        # 生成树结构
        tree = [[] for _ in range(n)]
        for (a, b) in roads:
            tree[a].append(b)
            tree[b].append(a)
        visited = [False] * n    # 标记数组
        visited[0] = True          # 初始标记0节点已遍历
        dfs(0)   # 从0节点开始深度优先搜索寻找每一条路径
        return self.fuel


