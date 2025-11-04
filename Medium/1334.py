class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 初始化距离矩阵，初始值为一个很大的数（表示不可达）
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]
        
        # 节点到自身的距离为0
        for i in range(n):
            dist[i][i] = 0
            
        # 根据边信息初始化直接相连的城市距离
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            
        # Floyd-Warshall算法计算所有城市对之间的最短距离
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # 统计每个城市在阈值内可到达的城市数量
        min_count = n  # 最小可达城市数初始化为最大值
        result_city = -1  # 结果城市编号
        
        for i in range(n):
            count = 0
            for j in range(n):
                # 排除自身，统计在阈值内的可达城市
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            
            # 更新最小可达城市数和结果城市
            # 当找到更小的可达城市数，或者相同数量但编号更大的城市时更新结果
            if count < min_count or (count == min_count and i > result_city):
                min_count = count
                result_city = i
                
        return result_city
