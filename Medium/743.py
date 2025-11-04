import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 构建图的邻接表表示
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 初始化距离字典，所有节点初始距离为无穷大
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0  # 起点到自己的距离为0
        
        # 使用优先队列（最小堆）来存储待处理的节点
        heap = [(0, k)]  # (距离, 节点)
        
        while heap:
            current_dist, current_node = heapq.heappop(heap)
            
            # 如果当前距离大于已知最短距离，跳过
            if current_dist > dist[current_node]:
                continue
                
            # 遍历当前节点的所有邻居
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                # 如果找到更短的路径，更新距离并加入堆
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        
        # 找出所有节点中的最大距离
        max_time = max(dist.values())
        
        # 如果存在不可达节点（距离仍为无穷大），返回-1
        return max_time if max_time < float('inf') else -1
