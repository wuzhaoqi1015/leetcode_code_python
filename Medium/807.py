class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 计算每行的最大值（西向天际线）
        row_max = [max(row) for row in grid]
        # 计算每列的最大值（北向天际线）
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        
        total_increase = 0
        # 遍历每个建筑物
        for i in range(n):
            for j in range(n):
                # 建筑物可增加到的最大高度是行最大值和列最大值中的较小值
                max_allowed = min(row_max[i], col_max[j])
                # 计算当前建筑物可增加的高度并累加
                total_increase += max_allowed - grid[i][j]
        
        return total_increase
