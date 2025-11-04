class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 使用动态规划，dp[i][j]表示以nums1[i-1]和nums2[j-1]结尾的最长公共子数组长度
        m, n = len(nums1), len(nums2)
        # 初始化dp数组，多一行一列用于处理边界情况
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        
        # 遍历两个数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前元素相等，则在前一个位置的基础上加1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # 更新最大长度
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                # 如果不相等，dp[i][j]保持为0（因为子数组要求连续）
        
        return max_len
