class Solution:
    def reorderSpaces(self, text: str) -> str:
        # 统计空格总数
        space_count = text.count(' ')
        
        # 分割单词，去除空字符串
        words = text.split()
        word_count = len(words)
        
        # 如果只有一个单词，所有空格放在末尾
        if word_count == 1:
            return words[0] + ' ' * space_count
        
        # 计算单词间空格数和末尾剩余空格数
        gap_count = word_count - 1
        spaces_between = space_count // gap_count
        spaces_end = space_count % gap_count
        
        # 构建结果字符串
        result = words[0]
        for i in range(1, word_count):
            result += ' ' * spaces_between + words[i]
        
        # 添加末尾剩余空格
        result += ' ' * spaces_end
        
        return result
