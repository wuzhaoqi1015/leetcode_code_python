class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 初始化左右指针和当前窗口开销
        left = 0
        current_cost = 0
        max_length = 0
        
        # 遍历字符串，右指针移动
        for right in range(len(s)):
            # 计算当前字符的开销并累加
            current_cost += abs(ord(s[right]) - ord(t[right]))
            
            # 如果当前开销超过预算，移动左指针缩小窗口
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length
