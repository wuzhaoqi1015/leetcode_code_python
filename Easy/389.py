class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 使用字典统计s中每个字符的出现次数
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # 遍历t中的每个字符，在字典中减去对应的计数
        for char in t:
            # 如果字符不在字典中或计数已经为0，说明这是被添加的字符
            if char not in char_count or char_count[char] == 0:
                return char
            # 减少对应字符的计数
            char_count[char] -= 1
        
        # 理论上不会执行到这里，但为了代码完整性返回空字符
        return ''
