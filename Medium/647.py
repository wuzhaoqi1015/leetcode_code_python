class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        # 中心扩展法：考虑奇数和偶数长度的回文
        for center in range(n):
            # 奇数长度回文，中心为单个字符
            left = center
            right = center
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            # 偶数长度回文，中心为两个字符之间的空隙
            left = center
            right = center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count
