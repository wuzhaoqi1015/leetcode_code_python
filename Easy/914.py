from typing import List
from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 统计每个数字出现的频率
        count = Counter(deck)
        # 获取所有频率值
        freq_values = list(count.values())
        # 计算所有频率值的最大公约数
        gcd_val = freq_values[0]
        for val in freq_values[1:]:
            gcd_val = math.gcd(gcd_val, val)
        # 最大公约数必须大于等于2才能满足分组条件
        return gcd_val >= 2
