class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_val = num
        min_val = num
        
        # 遍历所有可能的数字替换
        for digit in set(s):
            # 计算最大值：将digit替换为9
            max_candidate = int(s.replace(digit, '9'))
            # 计算最小值：将digit替换为0
            min_candidate = int(s.replace(digit, '0'))
            
            if max_candidate > max_val:
                max_val = max_candidate
            if min_candidate < min_val:
                min_val = min_candidate
        
        return max_val - min_val
