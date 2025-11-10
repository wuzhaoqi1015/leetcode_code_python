class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 遍历字符串，统计连续1的段数
        segment_count = 0
        n = len(s)
        i = 0
        
        while i < n:
            # 当遇到'1'时，开始一个新的连续1段
            if s[i] == '1':
                segment_count += 1
                # 如果已经超过1段，直接返回False
                if segment_count > 1:
                    return False
                # 跳过当前连续的所有'1'
                while i < n and s[i] == '1':
                    i += 1
            else:
                i += 1
        
        # 段数为0或1都返回True
        return True
