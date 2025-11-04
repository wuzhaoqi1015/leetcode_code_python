class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 对数组进行排序
        nums.sort()
        # 找到中位数
        median = nums[len(nums) // 2]
        # 计算所有元素与中位数的绝对差之和
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
