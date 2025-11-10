class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 对每一行进行排序，方便后续操作
        for i in range(len(grid)):
            grid[i].sort()
        
        ans = 0
        n = len(grid[0])
        
        # 从最后一列开始向前遍历（因为每行已排序，最大值在末尾）
        for j in range(n-1, -1, -1):
            max_val = 0
            # 遍历每一行，取当前列的最大值
            for i in range(len(grid)):
                max_val = max(max_val, grid[i][j])
            ans += max_val
        
        return ans
