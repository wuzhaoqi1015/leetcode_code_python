from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # 如果数组长度不能被k整除，直接返回False
        if len(nums) % k != 0:
            return False
            
        # 使用Counter统计每个数字的出现次数
        count = Counter(nums)
        # 对数组去重并排序
        sorted_nums = sorted(count.keys())
        
        # 遍历排序后的数字
        for num in sorted_nums:
            # 如果当前数字还有剩余
            if count[num] > 0:
                # 获取当前数字的出现次数
                current_count = count[num]
                # 检查从num开始的连续k个数字
                for i in range(num, num + k):
                    # 如果某个数字数量不足，返回False
                    if count[i] < current_count:
                        return False
                    # 减去当前组的数量
                    count[i] -= current_count
                    
        return True
