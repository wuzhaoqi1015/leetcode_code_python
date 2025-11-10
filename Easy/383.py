class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 如果勒索信长度大于杂志长度，直接返回False
        if len(ransomNote) > len(magazine):
            return False
            
        # 使用字典统计杂志中各字符出现次数
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
            
        # 检查勒索信中的每个字符是否都能从杂志中获取
        for char in ransomNote:
            # 如果字符不在杂志中或数量不足，返回False
            if char not in char_count or char_count[char] == 0:
                return False
            # 消耗一个字符
            char_count[char] -= 1
            
        return True
