class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 使用字典记录满足条件的子串出现次数
        substr_count = {}
        n = len(s)
        
        # 由于minSize<=maxSize，且子串长度越大出现次数可能越少
        # 实际上只需要考虑minSize长度的子串即可
        # 因为更长的子串出现次数不会超过相同起始位置的minSize子串
        size = minSize
        
        # 遍历所有长度为minSize的子串
        for i in range(n - size + 1):
            substr = s[i:i+size]
            
            # 检查子串中不同字母的数量
            unique_chars = len(set(substr))
            
            # 如果不同字母数量满足条件
            if unique_chars <= maxLetters:
                # 更新该子串的出现次数
                substr_count[substr] = substr_count.get(substr, 0) + 1
        
        # 如果没有满足条件的子串，返回0
        if not substr_count:
            return 0
        
        # 返回出现次数的最大值
        return max(substr_count.values())
