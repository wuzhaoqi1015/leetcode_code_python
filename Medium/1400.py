class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 如果k大于字符串长度，无法构造k个非空回文串
        if k > len(s):
            return False
        
        # 统计每个字符的出现次数
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # 统计出现奇数次的字符数量
        odd_count = 0
        for count in freq.values():
            if count % 2 == 1:
                odd_count += 1
        
        # 关键条件：奇数个字符的数量不能超过k
        # 因为每个回文串最多只能有一个字符出现奇数次（作为中心）
        # 同时k不能超过字符串长度（前面已经检查过）
        return odd_count <= k
