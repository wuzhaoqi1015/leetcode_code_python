class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 初始化第一个单词的字符计数作为基准
        base_count = [0] * 26
        for char in words[0]:
            base_count[ord(char) - ord('a')] += 1
        
        # 遍历剩余单词，更新最小字符计数
        for i in range(1, len(words)):
            current_count = [0] * 26
            for char in words[i]:
                current_count[ord(char) - ord('a')] += 1
            
            # 取每个字符的最小出现次数
            for j in range(26):
                base_count[j] = min(base_count[j], current_count[j])
        
        # 根据最小出现次数构建结果列表
        result = []
        for i in range(26):
            result.extend([chr(ord('a') + i)] * base_count[i])
        
        return result
