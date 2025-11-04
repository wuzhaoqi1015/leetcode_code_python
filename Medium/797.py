class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 使用深度优先搜索来遍历所有路径
        n = len(graph)  # 获取图的节点数量
        result = []  # 存储所有从0到n-1的路径
        path = []  # 存储当前遍历的路径
        
        def dfs(node):
            # 将当前节点加入路径
            path.append(node)
            
            # 如果当前节点是目标节点，将当前路径加入结果
            if node == n - 1:
                result.append(path[:])  # 使用切片复制当前路径
            else:
                # 遍历当前节点的所有邻居节点
                for neighbor in graph[node]:
                    dfs(neighbor)  # 递归访问邻居节点
            
            # 回溯，移除当前节点
            path.pop()
        
        # 从节点0开始深度优先搜索
        dfs(0)
        return result
