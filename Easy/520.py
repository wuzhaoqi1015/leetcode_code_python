class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 检查是否全大写
        if word.isupper():
            return True
        # 检查是否全小写
        if word.islower():
            return True
        # 检查是否只有首字母大写
        if word[0].isupper() and word[1:].islower():
            return True
        # 其他情况都不符合要求
        return False
