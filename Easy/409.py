class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 统计每个字符出现的频率
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        length = 0
        has_odd = False
        
        # 遍历所有字符频率
        for count in freq.values():
            if count % 2 == 0:
                # 偶数次字符全部使用
                length += count
            else:
                # 奇数次字符使用count-1次
                length += count - 1
                has_odd = True
        
        # 如果有奇数次字符，可以在中间放一个
        if has_odd:
            length += 1
            
        return length
