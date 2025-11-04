class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        
        result = []
        if len(s) < len(p):
            return result
            
        p_count = defaultdict(int)
        window_count = defaultdict(int)
        
        # 初始化p的字符计数
        for char in p:
            p_count[char] += 1
            
        # 初始化滑动窗口
        for i in range(len(p)):
            window_count[s[i]] += 1
            
        # 检查初始窗口
        if window_count == p_count:
            result.append(0)
            
        # 滑动窗口
        for i in range(len(p), len(s)):
            # 添加新字符
            window_count[s[i]] += 1
            # 移除旧字符
            left_char = s[i - len(p)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            # 检查当前窗口
            if window_count == p_count:
                result.append(i - len(p) + 1)
                
        return result
