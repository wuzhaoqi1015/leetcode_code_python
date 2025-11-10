class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 如果两个字符串相等，直接返回True
        if s1 == s2:
            return True
        
        # 找出所有不同的字符位置
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        # 如果不同位置的数量不是2，无法通过一次交换使字符串相等
        if len(diff) != 2:
            return False
        
        # 检查交换两个不同位置的字符后是否能使字符串相等
        i, j = diff[0], diff[1]
        return s1[i] == s2[j] and s1[j] == s2[i]
