class Solution:
    def sortSentence(self, s: str) -> str:
        # 将字符串按空格分割成单词列表
        words = s.split()
        # 创建一个列表用于存放按位置排序后的单词（不含数字）
        sorted_words = [''] * len(words)
        
        # 遍历每个单词
        for word in words:
            # 单词的最后一个字符是位置数字
            position = int(word[-1])
            # 提取单词部分（去掉最后一个数字字符）
            original_word = word[:-1]
            # 将单词放到对应的位置（位置从1开始，索引从0开始）
            sorted_words[position-1] = original_word
        
        # 用空格连接排序后的单词列表
        return ' '.join(sorted_words)
