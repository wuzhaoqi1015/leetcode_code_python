class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0  # 记录最长平衡子串长度
        n = len(s)
        
        # 遍历所有可能的起始位置
        for i in range(n):
            count0 = 0  # 记录0的数量
            count1 = 0  # 记录1的数量
            
            # 从当前位置开始向后扫描
            j = i
            while j < n:
                if s[j] == '0':
                    # 如果当前是0，但前面已经有1了，说明不符合"0在1之前"的条件
                    if count1 > 0:
                        break
                    count0 += 1
                else:  # s[j] == '1'
                    count1 += 1
                    # 当0和1数量相等时，更新最大长度
                    if count0 == count1:
                        max_len = max(max_len, count0 + count1)
                j += 1
        
        return max_len
