class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 使用字典记录每个字符第一次出现的位置
        first_occurrence = {}
        max_length = -1
        
        # 遍历字符串中的每个字符
        for i, char in enumerate(s):
            if char in first_occurrence:
                # 计算当前字符与第一次出现位置之间的子字符串长度
                current_length = i - first_occurrence[char] - 1
                # 更新最大长度
                if current_length > max_length:
                    max_length = current_length
            else:
                # 记录字符第一次出现的位置
                first_occurrence[char] = i
        
        return max_length
