class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 先对数组进行排序，这样我们只需要考虑后面的数整除前面的数
        nums.sort()
        n = len(nums)
        # dp[i]表示以nums[i]结尾的最大整除子集的长度
        dp = [1] * n
        # pre[i]记录在最大整除子集中，nums[i]的前一个元素的索引
        pre = [-1] * n
        
        max_len = 1  # 记录最大子集长度
        max_idx = 0  # 记录最大子集结尾元素的索引
        
        # 动态规划求解
        for i in range(n):
            for j in range(i):
                # 如果nums[i]能被nums[j]整除，且可以扩展子集
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j
            # 更新最大长度和对应索引
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        # 通过pre数组回溯构建结果
        result = []
        idx = max_idx
        while idx != -1:
            result.append(nums[idx])
            idx = pre[idx]
        
        # 由于是倒序添加的，需要反转结果
        return result[::-1]
