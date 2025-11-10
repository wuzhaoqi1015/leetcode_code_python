class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # 使用字典统计每个数字的出现次数
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        # 遍历字典，累加只出现一次的数字
        total = 0
        for num, count in count_dict.items():
            if count == 1:
                total += num
        
        return total
