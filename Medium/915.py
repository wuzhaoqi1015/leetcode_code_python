class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        # 从左到右记录当前位置及之前的最大值
        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i])
        
        # 从右到左记录当前位置及之后的最小值
        right_min = [0] * n
        right_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        
        # 寻找第一个位置使得左边最大值小于等于右边最小值
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                return i + 1
        return n
