class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 每次操作相当于将最大值减1，最终所有元素等于最小值
        # 因此总操作次数等于所有元素与最小值的差之和
        min_val = min(nums)
        total_moves = 0
        for num in nums:
            total_moves += num - min_val
        return total_moves
