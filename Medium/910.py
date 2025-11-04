class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # 先对数组进行排序
        nums.sort()
        n = len(nums)
        # 初始分数为整个数组的最大最小值差
        ans = nums[-1] - nums[0]
        
        # 遍历可能的切分点
        for i in range(n - 1):
            # 计算当前切分点下的最大值和最小值
            # 前半部分加k，后半部分减k
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            # 更新最小分数
            ans = min(ans, high - low)
        
        return ans
