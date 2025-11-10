class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # 使用字典统计每个数字出现的次数
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        pairs = 0
        remainder = 0
        
        # 遍历字典，计算数对数量和剩余数字数量
        for count in count_dict.values():
            pairs += count // 2  # 每个数字能形成的数对数量
            remainder += count % 2  # 每个数字剩余的单个数字数量
        
        return [pairs, remainder]
