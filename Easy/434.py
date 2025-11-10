class Solution:
    def countSegments(self, s: str) -> int:
        # 处理空字符串的情况
        if not s:
            return 0
            
        count = 0
        in_word = False  # 标记是否在单词中
        
        # 遍历字符串中的每个字符
        for char in s:
            if char != ' ':
                # 如果当前字符不是空格，且不在单词中，说明开始一个新单词
                if not in_word:
                    count += 1
                    in_word = True
            else:
                # 遇到空格，标记不在单词中
                in_word = False
                
        return count
