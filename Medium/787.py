from typing import List
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 构建邻接表表示图
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 初始化距离数组，记录到达每个节点的最小花费
        # 最多k次中转意味着最多k+1条边
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        
        # 使用队列进行BFS，队列元素为(当前节点, 当前花费)
        queue = collections.deque()
        queue.append((src, 0))
        stops = 0
        
        # 当还有中转次数且队列不为空时继续搜索
        while queue and stops <= k:
            # 当前层的节点数量
            level_size = len(queue)
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                current_node, current_cost = queue.popleft()
                
                # 遍历当前节点的所有邻居
                for neighbor, price in graph[current_node]:
                    new_cost = current_cost + price
                    # 如果新路径花费更少，则更新
                    if new_cost < dist[neighbor]:
                        dist[neighbor] = new_cost
                        queue.append((neighbor, new_cost))
            
            stops += 1
        
        # 返回结果，如果无法到达则返回-1
        return int(dist[dst]) if dist[dst] != INF else -1
