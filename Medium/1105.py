class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # dp[i]表示摆放前i本书的最小高度
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 没有书时高度为0
        
        for i in range(1, n + 1):
            width = 0
            height = 0
            # 尝试将第j到第i本书放在同一层
            for j in range(i, 0, -1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j-1][1])
                # 状态转移：前j-1本书的最小高度加上当前层高度
                dp[i] = min(dp[i], dp[j-1] + height)
        
        return dp[n]
