class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表存储数字和对应的索引
        num_dict = {}
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算需要的补数
            complement = target - num
            # 如果补数在哈希表中，返回结果
            if complement in num_dict:
                return [num_dict[complement], i]
            # 将当前数字和索引存入哈希表
            num_dict[num] = i
        # 根据题目假设，总会有一个解，所以这里不会执行到
        return []
