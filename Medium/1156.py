class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符的总出现次数
        from collections import Counter
        total_count = Counter(text)
        
        # 将连续相同字符分组
        groups = []
        i = 0
        n = len(text)
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j
        
        # 情况1：直接取最长连续子串
        max_len = max(min(length + 1, total_count[char]) for char, length in groups)
        
        # 情况2：合并两个相邻的相同字符组（中间隔了一个不同字符）
        for i in range(1, len(groups) - 1):
            if groups[i-1][0] == groups[i+1][0] and groups[i][1] == 1:
                char = groups[i-1][0]
                total = groups[i-1][1] + groups[i+1][1]
                # 如果还有其他相同字符可用，可以多连一个
                if total < total_count[char]:
                    total += 1
                max_len = max(max_len, total)
        
        return max_len
