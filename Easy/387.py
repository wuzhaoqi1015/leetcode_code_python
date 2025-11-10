class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 使用字典记录每个字符出现的次数
        char_count = {}
        # 第一次遍历，统计每个字符出现的频率
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        # 第二次遍历，找到第一个出现次数为1的字符并返回其索引
        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx
        # 如果没有找到不重复的字符，返回-1
        return -1
