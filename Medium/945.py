class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 首先对数组进行排序
        nums.sort()
        moves = 0
        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            # 如果当前元素小于等于前一个元素，需要增加到前一个元素+1
            if nums[i] <= nums[i-1]:
                # 计算需要增加的次数
                increment = nums[i-1] - nums[i] + 1
                # 更新当前元素的值
                nums[i] += increment
                # 累加操作次数
                moves += increment
        return moves
