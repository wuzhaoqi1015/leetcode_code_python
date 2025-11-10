class NumArray:
    def __init__(self, nums: List[int]):
        # 初始化前缀和数组，长度为原数组长度+1
        self.prefix_sum = [0] * (len(nums) + 1)
        # 计算前缀和
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 通过前缀和数组计算区间和
        return self.prefix_sum[right+1] - self.prefix_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
