class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 使用并查集解决连通分量问题
        parent = {}  # 存储每个节点的父节点
        rank = {}    # 存储每个节点的秩
        
        # 查找根节点，带路径压缩
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 合并两个集合，按秩合并
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
        
        # 初始化并查集
        for stone in stones:
            x, y = stone
            # 将x坐标和y坐标映射到不同的域，避免冲突
            node_x = x
            node_y = y + 10001  # 偏移y坐标，确保不与x坐标冲突
            if node_x not in parent:
                parent[node_x] = node_x
                rank[node_x] = 0
            if node_y not in parent:
                parent[node_y] = node_y
                rank[node_y] = 0
            # 将同一石头的x坐标和y坐标合并
            union(node_x, node_y)
        
        # 统计连通分量的数量
        roots = set()
        for node in parent:
            roots.add(find(node))
        
        # 最大可移除石头数量 = 总石头数 - 连通分量数量
        return len(stones) - len(roots)
