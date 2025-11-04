class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 对字典按长度降序、字典序升序排序
        dictionary.sort(key=lambda x: (-len(x), x))
        
        # 检查word是否是s的子序列
        def is_subsequence(word, s):
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)
        
        # 遍历排序后的字典，找到第一个满足条件的字符串
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        
        return ""
