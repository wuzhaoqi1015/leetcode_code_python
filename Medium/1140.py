class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        dp = [[0] * (n + 1) for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        next_m = max(m, x)
                        opponent_score = dp[i + x][next_m]
                        current_score = suffix_sum[i] - opponent_score
                        if current_score > dp[i][m]:
                            dp[i][m] = current_score
        
        return dp[0][1]
