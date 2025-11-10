class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 如果s是空字符串，则一定是t的子序列
        if not s:
            return True
        # 如果t的长度小于s，则s不可能是t的子序列
        if len(t) < len(s):
            return False
            
        i, j = 0, 0  # i指向s的当前位置，j指向t的当前位置
        
        # 双指针遍历两个字符串
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # 字符匹配成功
                i += 1  # 移动到s的下一个字符
            j += 1  # 无论是否匹配，t的指针都要前进
            
        # 如果s的所有字符都匹配成功，则返回True
        return i == len(s)
