class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        # 遍历数组，利用索引标记出现过的数字
        for i in range(len(nums)):
            # 获取当前数字的绝对值
            num = abs(nums[i])
            # 计算对应的索引位置
            idx = num - 1
            # 如果该位置的数字已经是负数，说明之前出现过
            if nums[idx] < 0:
                result.append(num)
            else:
                # 否则将对应位置的数字取反标记
                nums[idx] = -nums[idx]
        return result
