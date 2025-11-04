class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        # 对于长度大于2的情况，最大值总是通过将第一个数除以后面所有数的连除结果得到
        # 即 nums[0]/(nums[1]/nums[2]/.../nums[n-1])
        result = f"{nums[0]}/({nums[1]}"
        for i in range(2, n):
            result += f"/{nums[i]}"
        result += ")"
        return result
