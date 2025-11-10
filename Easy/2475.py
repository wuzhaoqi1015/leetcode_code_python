class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        # 三重循环枚举所有可能的三元组
        for i in range(n):
            for j in range(i + 1, n):
                # 前两个数不同才继续检查第三个
                if nums[i] != nums[j]:
                    for k in range(j + 1, n):
                        # 检查三个数是否两两不同
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            count += 1
        return count
