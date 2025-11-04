class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 初始化一个长度为26的数组来记录每个字符的频率差
        freq = [0] * 26
        
        # 遍历字符串s和t，统计字符频率差
        for i in range(len(s)):
            # s中的字符频率加1
            freq[ord(s[i]) - ord('a')] += 1
            # t中的字符频率减1
            freq[ord(t[i]) - ord('a')] -= 1
        
        # 计算需要替换的步骤数
        steps = 0
        for count in freq:
            # 只考虑频率差为正的情况，表示s中多出的字符需要被替换
            if count > 0:
                steps += count
        
        return steps
