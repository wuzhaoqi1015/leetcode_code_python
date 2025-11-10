class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()  # 使用集合记录已经出现过的字符
        for char in s:  # 遍历字符串中的每个字符
            if char in seen:  # 如果字符已经在集合中，说明是第二次出现
                return char  # 立即返回该字符
            seen.add(char)  # 将当前字符添加到集合中
