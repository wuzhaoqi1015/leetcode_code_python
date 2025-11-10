class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 创建字符到索引的映射字典
        char_order = {}
        for idx, char in enumerate(order):
            char_order[char] = idx
        
        # 遍历单词列表，检查每对相邻单词
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # 比较两个单词的每个字符
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                # 如果字符不同，检查顺序
                if word1[j] != word2[j]:
                    if char_order[word1[j]] > char_order[word2[j]]:
                        return False
                    break  # 找到第一个不同字符后跳出循环
            else:
                # 如果前面字符都相同，检查单词长度
                if len(word1) > len(word2):
                    return False
        
        return True
