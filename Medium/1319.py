class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 如果连接数少于n-1，则无法连接所有计算机
        if len(connections) < n - 1:
            return -1
            
        # 构建并查集类
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
                self.count = n  # 记录连通分量个数
                
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
                
            def union(self, x, y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx == rooty:
                    return False  # 已经连通，不需要合并
                    
                # 按秩合并
                if self.rank[rootx] < self.rank[rooty]:
                    self.parent[rootx] = rooty
                elif self.rank[rootx] > self.rank[rooty]:
                    self.parent[rooty] = rootx
                else:
                    self.parent[rooty] = rootx
                    self.rank[rootx] += 1
                    
                self.count -= 1
                return True
                
        # 初始化并查集
        uf = UnionFind(n)
        redundant = 0  # 记录冗余连接数
        
        # 遍历所有连接
        for a, b in connections:
            if not uf.union(a, b):
                redundant += 1
                
        # 需要的操作次数等于连通分量个数减1
        # 但需要确保有足够的冗余连接
        if redundant >= uf.count - 1:
            return uf.count - 1
        else:
            return -1
