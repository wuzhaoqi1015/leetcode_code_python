class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 将字符串s按空格分割成单词列表
        words = s.split()
        
        # 如果pattern长度和单词数量不匹配，直接返回False
        if len(pattern) != len(words):
            return False
        
        # 创建两个字典来维护双向映射关系
        char_to_word = {}  # 字符到单词的映射
        word_to_char = {}  # 单词到字符的映射
        
        # 同时遍历pattern中的字符和words中的单词
        for char, word in zip(pattern, words):
            # 检查字符到单词的映射是否一致
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # 检查单词到字符的映射是否一致
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        # 所有映射关系都一致，返回True
        return True
