class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # 使用哈希表存储每个值的索引，便于快速查找
        index_map = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        # dp[i][j] 表示以arr[i]和arr[j]结尾的斐波那契序列的最大长度
        dp = [[0] * n for _ in range(n)]
        max_len = 0
        
        # 遍历所有可能的结尾对(i,j)
        for j in range(n):
            for i in range(j):
                # 计算前一个斐波那契数
                prev = arr[j] - arr[i]
                # 如果前一个数存在且在i之前
                if prev in index_map and index_map[prev] < i:
                    k = index_map[prev]
                    # 更新dp[i][j]为dp[k][i] + 1，至少为3
                    dp[i][j] = dp[k][i] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    # 如果没有前一个数，初始化为2
                    dp[i][j] = 2
        
        # 如果找到的序列长度大于2则返回，否则返回0
        return max_len if max_len >= 3 else 0
