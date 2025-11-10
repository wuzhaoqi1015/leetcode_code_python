class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 使用字典统计每个数字的出现次数
        count_dict = {}
        for num in arr:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        # 将出现次数存入集合，检查是否有重复
        occurrences = set()
        for count in count_dict.values():
            if count in occurrences:
                return False
            occurrences.add(count)
        
        return True
