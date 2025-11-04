class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # 将每个1x1方格划分为4个三角形区域，编号为0,1,2,3
        # 0: 上三角, 1: 右三角, 2: 下三角, 3: 左三角
        parent = [i for i in range(4 * n * n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        for i in range(n):
            for j in range(n):
                idx = 4 * (i * n + j)  # 当前方格的起始索引
                char = grid[i][j]
                
                # 方格内部的连接
                if char == ' ':
                    # 空格：连接所有4个三角形
                    union(idx, idx + 1)
                    union(idx, idx + 2)
                    union(idx, idx + 3)
                elif char == '/':
                    # '/'：连接0和3，1和2
                    union(idx, idx + 3)
                    union(idx + 1, idx + 2)
                else:  # '\'
                    # '\'：连接0和1，2和3
                    union(idx, idx + 1)
                    union(idx + 2, idx + 3)
                
                # 与右边方格的连接（当前方格的1与右边方格的3连接）
                if j + 1 < n:
                    right_idx = 4 * (i * n + j + 1)
                    union(idx + 1, right_idx + 3)
                
                # 与下方方格的连接（当前方格的2与下方方格的0连接）
                if i + 1 < n:
                    down_idx = 4 * ((i + 1) * n + j)
                    union(idx + 2, down_idx)
        
        # 统计连通分量的数量
        regions = set()
        for i in range(4 * n * n):
            regions.add(find(i))
        
        return len(regions)
