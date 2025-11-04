class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n  # 记录城市是否被访问过
        provinces = 0  # 省份计数器
        
        def dfs(city):
            # 深度优先搜索遍历与当前城市相连的所有城市
            visited[city] = True
            for neighbor in range(n):
                # 如果邻居城市未被访问且与当前城市相连
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        # 遍历所有城市
        for i in range(n):
            if not visited[i]:
                # 发现新的省份，执行DFS遍历该省份所有城市
                provinces += 1
                dfs(i)
        
        return provinces
