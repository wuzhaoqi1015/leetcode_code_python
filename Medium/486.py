class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # 创建dp数组，dp[i][j]表示在数组nums[i:j+1]中当前玩家能获得的最大净胜分
        dp = [[0] * n for _ in range(n)]
        
        # 初始化对角线元素，当只有一个元素时，当前玩家获得该元素
        for i in range(n):
            dp[i][i] = nums[i]
        
        # 填充dp数组，从右下角开始向上填充
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # 当前玩家可以选择左端或右端元素，然后减去对手在剩余数组中能获得的最大净胜分
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        # 如果玩家1在完整数组中的净胜分大于等于0，则玩家1获胜
        return dp[0][n-1] >= 0
