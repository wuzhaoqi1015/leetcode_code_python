class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        count = 0
        # 遍历所有可能的3x3子矩阵的左上角位置
        for i in range(rows - 2):
            for j in range(cols - 2):
                # 检查当前3x3子矩阵是否为幻方
                if self.isMagicSquare(grid, i, j):
                    count += 1
        return count
    
    def isMagicSquare(self, grid, x, y):
        # 检查是否包含1-9的所有数字且不重复
        nums = set()
        for i in range(3):
            for j in range(3):
                num = grid[x + i][y + j]
                if num < 1 or num > 9:
                    return False
                nums.add(num)
        if len(nums) != 9:
            return False
        
        # 计算第一行的和作为目标值
        target = grid[x][y] + grid[x][y + 1] + grid[x][y + 2]
        
        # 检查其他两行
        for i in range(1, 3):
            row_sum = grid[x + i][y] + grid[x + i][y + 1] + grid[x + i][y + 2]
            if row_sum != target:
                return False
        
        # 检查三列
        for j in range(3):
            col_sum = grid[x][y + j] + grid[x + 1][y + j] + grid[x + 2][y + j]
            if col_sum != target:
                return False
        
        # 检查两条对角线
        diag1 = grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2]
        diag2 = grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y]
        if diag1 != target or diag2 != target:
            return False
        
        return True
