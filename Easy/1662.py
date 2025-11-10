class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 直接拼接两个字符串数组并比较
        return ''.join(word1) == ''.join(word2)
