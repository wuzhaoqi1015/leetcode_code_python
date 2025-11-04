class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 使用滑动窗口方法，维护窗口内字符频率
        left = 0
        max_count = 0
        char_count = {}
        max_length = 0
        
        for right in range(len(s)):
            # 更新当前字符的计数
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            # 更新窗口内出现最多次数字符的次数
            max_count = max(max_count, char_count[s[right]])
            
            # 如果窗口长度减去最多字符次数大于k，需要收缩窗口
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length
