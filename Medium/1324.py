class Solution:
    def printVertically(self, s: str) -> List[str]:
        # 将字符串按空格分割成单词列表
        words = s.split()
        # 找到最长单词的长度作为列数
        max_len = max(len(word) for word in words)
        # 初始化结果列表
        result = []
        
        # 遍历每一列
        for i in range(max_len):
            col_chars = []
            # 遍历每个单词
            for word in words:
                # 如果当前列索引在单词长度范围内，取对应字符，否则用空格
                if i < len(word):
                    col_chars.append(word[i])
                else:
                    col_chars.append(' ')
            # 将字符列表转换为字符串
            col_str = ''.join(col_chars)
            # 去除字符串末尾的空格
            col_str = col_str.rstrip()
            # 将处理后的字符串加入结果列表
            result.append(col_str)
        
        return result
