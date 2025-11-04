from itertools import permutations
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # 生成所有可能的4位数排列
        perms = permutations(arr)
        max_time = -1
        result = ""
        
        # 遍历所有排列组合
        for h1, h2, m1, m2 in perms:
            # 计算小时和分钟
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            
            # 检查时间是否有效
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                # 计算总分钟数作为比较基准
                total_minutes = hours * 60 + minutes
                # 更新最大时间
                if total_minutes > max_time:
                    max_time = total_minutes
                    result = f"{h1}{h2}:{m1}{m2}"
        
        return result
