class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # 检查s是否是t的子序列
        def is_subsequence(s, t):
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        
        # 按字符串长度降序排序
        strs.sort(key=len, reverse=True)
        
        # 检查每个字符串是否是特殊序列
        for i in range(len(strs)):
            is_special = True
            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    is_special = False
                    break
            if is_special:
                return len(strs[i])
        
        return -1
