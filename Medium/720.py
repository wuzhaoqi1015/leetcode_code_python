class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 对单词列表进行排序，先按长度升序，再按字典序升序
        words.sort()
        words.sort(key=len)
        
        # 使用集合存储所有单词
        word_set = set(words)
        longest_word = ""
        
        # 遍历每个单词
        for word in words:
            valid = True
            # 检查单词的所有前缀是否都在集合中
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            
            # 如果单词有效，更新最长单词
            if valid:
                # 如果当前单词更长，或者长度相同但字典序更小
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        
        return longest_word
