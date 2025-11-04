class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 使用集合存储所有单词的后缀
        word_set = set(words)
        
        # 对于每个单词，移除其所有可能的后缀
        for word in words:
            for i in range(1, len(word)):
                # 如果单词的后缀在集合中，则移除该后缀
                suffix = word[i:]
                if suffix in word_set:
                    word_set.discard(suffix)
        
        # 计算最终编码长度：每个保留单词的长度加1（#号），然后求和
        return sum(len(word) + 1 for word in word_set)
