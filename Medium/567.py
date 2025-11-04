class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 如果s1长度大于s2，直接返回False
        if len(s1) > len(s2):
            return False
            
        # 初始化两个长度为26的数组来记录字符频率
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # 统计s1和s2前len(s1)个字符的频率
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # 初始化匹配计数
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # 滑动窗口遍历s2的剩余部分
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # 处理右指针新加入的字符
            index = ord(s2[right]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches -= 1
                
            # 处理左指针移出的字符
            index = ord(s2[left]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] - 1:
                matches -= 1
                
            left += 1
            
        # 检查最后一个窗口
        return matches == 26
