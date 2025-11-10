class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # 将句子按空格分割成单词列表
        words = sentence.split()
        n = len(words)
        
        # 如果只有一个单词，检查首尾字符是否相同
        if n == 1:
            return words[0][0] == words[0][-1]
        
        # 检查相邻单词的连接性
        for i in range(n - 1):
            current_word = words[i]
            next_word = words[i + 1]
            # 当前单词的最后一个字符与下一个单词的第一个字符比较
            if current_word[-1] != next_word[0]:
                return False
        
        # 检查最后一个单词与第一个单词的连接性
        if words[-1][-1] != words[0][0]:
            return False
        
        return True
