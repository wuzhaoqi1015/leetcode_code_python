class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 创建一个与nums相同长度的结果数组
        ans = [0] * len(nums)
        # 遍历数组，根据题目要求构建ans
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
