class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 使用字典记录以每个数字结尾的最长子序列长度
        dp = {}
        max_length = 1
        
        for num in arr:
            # 查找当前数字的前一个数字是否存在
            prev = num - difference
            # 如果前一个数字存在，则当前数字的序列长度加1
            if prev in dp:
                dp[num] = dp[prev] + 1
            else:
                # 否则当前数字作为序列起点
                dp[num] = 1
            # 更新最大长度
            max_length = max(max_length, dp[num])
        
        return max_length
