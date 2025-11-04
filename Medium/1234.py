from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4  # 每个字符应该出现的次数
        
        # 统计整个字符串中每个字符的出现次数
        count = Counter(s)
        
        # 如果已经是平衡字符串，直接返回0
        if all(count[ch] == target for ch in 'QWER'):
            return 0
        
        left = 0
        min_len = n  # 初始化最小长度为整个字符串长度
        
        # 使用滑动窗口，窗口内的字符是我们将要替换的部分
        # 窗口外的字符需要满足不超过target
        for right in range(n):
            # 右指针移动，减少对应字符的计数（表示这个字符被包含在窗口内）
            count[s[right]] -= 1
            
            # 当窗口外的所有字符计数都不超过target时，尝试收缩左指针
            while left <= right and all(count[ch] <= target for ch in 'QWER'):
                # 更新最小长度
                min_len = min(min_len, right - left + 1)
                # 左指针移动，增加对应字符的计数（表示这个字符不再在窗口内）
                count[s[left]] += 1
                left += 1
        
        return min_len
