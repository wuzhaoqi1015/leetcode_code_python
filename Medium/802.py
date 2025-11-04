class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 状态数组：0-未访问，1-访问中/在环中，2-安全节点
        state = [0] * n
        
        def dfs(node):
            # 如果当前节点已被访问过，检查状态
            if state[node] != 0:
                return state[node] == 2
            # 标记为访问中
            state[node] = 1
            # 遍历所有邻居节点
            for neighbor in graph[node]:
                # 如果邻居节点在环中或不安全，则当前节点也不安全
                if not dfs(neighbor):
                    return False
            # 所有邻居都安全，标记当前节点为安全
            state[node] = 2
            return True
        
        result = []
        # 检查每个节点是否安全
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result
