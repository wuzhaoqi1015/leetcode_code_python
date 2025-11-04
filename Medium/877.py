class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j] 表示从第i堆到第j堆石子，当前玩家能比对手多得的石子数
        dp = [[0] * n for _ in range(n)]
        
        # 初始化：当只有一堆石子时，当前玩家能比对手多得的石子数就是这堆石子的数量
        for i in range(n):
            dp[i][i] = piles[i]
        
        # 从长度为2的子数组开始计算
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 当前玩家可以选择拿左边或右边的石子堆
                # 选择左边：当前玩家得到piles[i]，对手从i+1到j堆中能获得的最大优势是dp[i+1][j]
                # 选择右边：当前玩家得到piles[j]，对手从i到j-1堆中能获得的最大优势是dp[i][j-1]
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        # 如果从0到n-1堆中，Alice能比Bob多得石子数大于0，则Alice获胜
        return dp[0][n - 1] > 0
