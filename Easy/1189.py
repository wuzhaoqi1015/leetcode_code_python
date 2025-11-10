class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 统计text中每个字符的出现次数
        from collections import Counter
        text_count = Counter(text)
        
        # 统计"balloon"中每个字符的出现次数
        target = "balloon"
        target_count = Counter(target)
        
        # 计算每个字符能组成的最大气球数量
        result = float('inf')
        for char in target_count:
            # 当前字符在text中的数量除以在目标单词中的数量
            char_max = text_count[char] // target_count[char]
            result = min(result, char_max)
        
        return result
