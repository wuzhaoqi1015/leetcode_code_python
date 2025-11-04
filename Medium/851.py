class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]  # 构建有向图，记录比当前节点穷的人
        indegree = [0] * n  # 记录每个节点的入度
        
        # 构建图结构，a比b有钱，建立a->b的边
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        # 初始化结果数组，开始时每个人自身就是答案
        answer = list(range(n))
        
        # 使用队列进行拓扑排序
        queue = collections.deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            # 遍历比当前节点穷的所有邻居
            for neighbor in graph[current]:
                # 更新邻居的答案：选择安静值更小的那个人
                if quiet[answer[current]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[current]
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return answer
