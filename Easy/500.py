class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # 定义键盘三行字符
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            # 将单词转换为小写
            lower_word = word.lower()
            # 检查单词所有字符是否在同一行
            if set(lower_word).issubset(row1) or set(lower_word).issubset(row2) or set(lower_word).issubset(row3):
                result.append(word)
        return result
