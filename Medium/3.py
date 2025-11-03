class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用滑动窗口和哈希表来记录字符最后出现的位置
        char_index = {}  # 存储字符及其最后出现的索引
        left = 0  # 滑动窗口的左边界
        max_length = 0  # 记录最长子串的长度
        
        for right in range(len(s)):
            # 如果当前字符已经在窗口中，并且其索引大于等于左边界
            if s[right] in char_index and char_index[s[right]] >= left:
                # 移动左边界到重复字符的下一个位置
                left = char_index[s[right]] + 1
            # 更新当前字符的索引
            char_index[s[right]] = right
            # 计算当前窗口的长度并更新最大值
            max_length = max(max_length, right - left + 1)
        
        return max_length
