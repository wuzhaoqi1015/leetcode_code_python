class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 使用字典统计每个标准化骨牌的出现次数
        count_dict = {}
        for domino in dominoes:
            # 将骨牌标准化为元组形式，确保小的数字在前
            normalized = tuple(sorted(domino))
            count_dict[normalized] = count_dict.get(normalized, 0) + 1
        
        # 计算等价骨牌对的数量
        result = 0
        for count in count_dict.values():
            # 使用组合数公式 C(n,2) = n*(n-1)//2
            if count >= 2:
                result += count * (count - 1) // 2
                
        return result
