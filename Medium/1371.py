class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 使用状态压缩，5位二进制数表示5个元音字母的奇偶状态
        # 初始状态为0，表示所有元音字母都出现偶数次
        first_occurrence = {0: -1}  # 记录每个状态第一次出现的位置
        state = 0  # 当前状态
        max_len = 0  # 最长子串长度
        
        # 元音字母对应的位掩码
        vowel_mask = {
            'a': 1,    # 00001
            'e': 2,    # 00010  
            'i': 4,    # 00100
            'o': 8,    # 01000
            'u': 16    # 10000
        }
        
        for i, char in enumerate(s):
            if char in vowel_mask:
                # 遇到元音字母，翻转对应位的状态
                state ^= vowel_mask[char]
            
            # 如果当前状态之前出现过，说明这两个位置之间的子串满足条件
            if state in first_occurrence:
                max_len = max(max_len, i - first_occurrence[state])
            else:
                # 记录状态第一次出现的位置
                first_occurrence[state] = i
        
        return max_len
