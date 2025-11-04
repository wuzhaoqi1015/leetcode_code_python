class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 初始化动态规划数组，dp[i][j]表示使用i个0和j个1时能构成的最大子集长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 遍历每个字符串
        for s in strs:
            # 统计当前字符串中0和1的数量
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # 从后往前更新dp数组，避免重复计算
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # 状态转移方程：选择当前字符串或不选择当前字符串
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]
