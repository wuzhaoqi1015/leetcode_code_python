class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        # 记录最近一次出现a、b、c的位置
        last_pos = [-1, -1, -1]
        
        for i in range(n):
            # 更新当前字符对应的最新位置
            if s[i] == 'a':
                last_pos[0] = i
            elif s[i] == 'b':
                last_pos[1] = i
            else:  # s[i] == 'c'
                last_pos[2] = i
            
            # 如果三个字符都至少出现了一次
            if min(last_pos) != -1:
                # 以i结尾的包含abc的子串数量等于最小位置+1
                count += min(last_pos) + 1
        
        return count
