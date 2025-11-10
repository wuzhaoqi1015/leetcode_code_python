class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 统计chars中每个字符的出现次数
        from collections import Counter
        chars_count = Counter(chars)
        total_length = 0
        
        # 遍历words中的每个单词
        for word in words:
            word_count = Counter(word)  # 统计当前单词的字符频率
            valid = True
            
            # 检查当前单词的所有字符是否都能在chars中找到足够数量
            for char, count in word_count.items():
                if chars_count[char] < count:
                    valid = False
                    break
            
            # 如果单词有效，累加其长度
            if valid:
                total_length += len(word)
        
        return total_length
