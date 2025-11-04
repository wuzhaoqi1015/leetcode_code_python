class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))  # 初始化并查集，每个节点的父节点初始化为自己
        
        def find(x):
            # 查找根节点，并进行路径压缩
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # 合并两个节点所在的集合
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False  # 如果两个节点已经在同一集合中，说明形成了环
            parent[root_x] = root_y
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]  # 当发现形成环的边时，返回这条边
