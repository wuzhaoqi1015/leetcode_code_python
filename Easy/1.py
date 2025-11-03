class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用字典存储已遍历元素的值和索引
        num_dict = {}
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算当前元素所需的补数
            complement = target - num
            # 检查补数是否在字典中
            if complement in num_dict:
                # 如果存在，返回补数的索引和当前索引
                return [num_dict[complement], i]
            # 将当前元素的值和索引存入字典
            num_dict[num] = i
        # 根据题目假设，总会存在一个有效答案，所以这里不需要返回默认值
