class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[i][j]表示从i到j的最小代价
        dp = [[0] * n for _ in range(n)]
        # max_val[i][j]表示从i到j的最大值
        max_val = [[0] * n for _ in range(n)]
        
        # 初始化max_val数组
        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i + 1, n):
                max_val[i][j] = max(max_val[i][j-1], arr[j])
        
        # 动态规划计算最小代价
        for length in range(2, n + 1):  # 区间长度从2开始
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                # 枚举分割点k，将区间[i,j]分成[i,k]和[k+1,j]
                for k in range(i, j):
                    # 当前区间的代价 = 左子树代价 + 右子树代价 + 根节点代价
                    # 根节点代价 = 左子树最大值 * 右子树最大值
                    cost = dp[i][k] + dp[k+1][j] + max_val[i][k] * max_val[k+1][j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        
        return dp[0][n-1]
