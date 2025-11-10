class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果两个字符串长度不同，直接返回False
        if len(s) != len(t):
            return False
        
        # 使用字典统计每个字符的出现次数
        char_count = {}
        
        # 遍历字符串s，统计字符出现次数
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # 遍历字符串t，减少字符出现次数
        for char in t:
            # 如果字符不在字典中或出现次数为0，返回False
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        # 检查所有字符计数是否归零
        for count in char_count.values():
            if count != 0:
                return False
        
        return True
