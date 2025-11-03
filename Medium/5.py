class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        
        # 遍历每个字符，以每个字符为中心向两边扩展
        for i in range(len(s)):
            # 奇数长度回文
            len1 = self.expandAroundCenter(s, i, i)
            # 偶数长度回文
            len2 = self.expandAroundCenter(s, i, i + 1)
            # 取较长的回文长度
            max_len = max(len1, len2)
            
            # 如果找到更长的回文，更新起始和结束位置
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 从中心向两边扩展，直到不再是回文
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回回文长度
        return right - left - 1
