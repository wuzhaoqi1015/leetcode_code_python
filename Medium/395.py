class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 使用分治法解决该问题
        if len(s) < k:
            return 0
        
        # 统计字符频率
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # 找到第一个不满足条件的字符作为分割点
        split_char = None
        for char in freq:
            if freq[char] < k:
                split_char = char
                break
        
        # 如果没有分割点，说明整个字符串都满足条件
        if split_char is None:
            return len(s)
        
        # 按分割点分割字符串并递归求解
        max_len = 0
        for substr in s.split(split_char):
            max_len = max(max_len, self.longestSubstring(substr, k))
        
        return max_len
