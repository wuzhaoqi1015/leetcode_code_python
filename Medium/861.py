class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 确保第一列全部为1，通过行翻转实现
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
        # 对于每一列，如果0的数量多于1的数量，则翻转该列
        for j in range(1, n):
            zero_count = 0
            for i in range(m):
                if grid[i][j] == 0:
                    zero_count += 1
            if zero_count > m - zero_count:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        # 计算总分
        total_score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = row_value * 2 + grid[i][j]
            total_score += row_value
        
        return total_score
