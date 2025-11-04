from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 如果牌的总数不能被groupSize整除，直接返回False
        if len(hand) % groupSize != 0:
            return False
            
        # 使用Counter统计每张牌的数量
        count = Counter(hand)
        # 对所有的牌值进行排序
        sorted_keys = sorted(count.keys())
        
        # 遍历排序后的牌值
        for num in sorted_keys:
            # 如果当前牌的数量大于0
            if count[num] > 0:
                # 获取当前牌的数量作为起始数量
                start_count = count[num]
                # 检查从num开始的连续groupSize张牌
                for i in range(groupSize):
                    current_num = num + i
                    # 如果当前数字不存在或数量不足，返回False
                    if count[current_num] < start_count:
                        return False
                    # 减去起始数量的牌
                    count[current_num] -= start_count
        
        return True
