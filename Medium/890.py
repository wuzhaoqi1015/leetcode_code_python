class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            # 创建两个字典来存储字符映射关系
            word_to_pattern = {}
            pattern_to_word = {}
            
            # 遍历单词和模式的每个字符
            for w_char, p_char in zip(word, pattern):
                # 检查单词到模式的映射是否一致
                if w_char in word_to_pattern:
                    if word_to_pattern[w_char] != p_char:
                        return False
                else:
                    word_to_pattern[w_char] = p_char
                
                # 检查模式到单词的映射是否一致
                if p_char in pattern_to_word:
                    if pattern_to_word[p_char] != w_char:
                        return False
                else:
                    pattern_to_word[p_char] = w_char
                    
            return True
        
        result = []
        # 遍历所有单词，检查是否匹配模式
        for word in words:
            if match(word):
                result.append(word)
                
        return result
