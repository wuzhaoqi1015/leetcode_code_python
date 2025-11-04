class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 获取两个数组的长度
        m, n = len(nums1), len(nums2)
        # 创建动态规划表，大小为(m+1) x (n+1)，初始化为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 遍历两个数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前元素相等，可以连接一条线
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 否则取左边或上边的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 返回右下角的值，即最大连线数
        return dp[m][n]
