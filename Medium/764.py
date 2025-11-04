class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 创建网格并初始化为1
        grid = [[1] * n for _ in range(n)]
        # 将地雷位置设为0
        for x, y in mines:
            grid[x][y] = 0
        
        # 创建四个方向的DP数组
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        
        # 计算从左到右的连续1个数
        for i in range(n):
            count = 0
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                left[i][j] = count
        
        # 计算从右到左的连续1个数
        for i in range(n):
            count = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                right[i][j] = count
        
        # 计算从上到下的连续1个数
        for j in range(n):
            count = 0
            for i in range(n):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                up[i][j] = count
        
        # 计算从下到上的连续1个数
        for j in range(n):
            count = 0
            for i in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                down[i][j] = count
        
        # 计算每个位置能形成的最大加号阶数
        max_order = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # 取四个方向的最小值作为当前点的阶数
                    order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                    max_order = max(max_order, order)
        
        return max_order
