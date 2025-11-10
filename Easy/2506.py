class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 将每个单词转换为字符集合，然后转换为排序后的元组作为特征
        features = []
        for word in words:
            # 使用frozenset来确保可哈希，但题目要求相同字符组成，所以用排序元组更准确
            char_set = tuple(sorted(set(word)))
            features.append(char_set)
        
        count = 0
        n = len(words)
        # 遍历所有下标对 (i, j)，其中 i < j
        for i in range(n):
            for j in range(i + 1, n):
                # 如果两个单词的特征相同，则计数加1
                if features[i] == features[j]:
                    count += 1
                    
        return count
