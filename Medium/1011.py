class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 最小运载能力至少是最大单个包裹重量
        left = max(weights)
        # 最大运载能力是所有包裹重量之和
        right = sum(weights)
        
        # 二分查找寻找最低运载能力
        while left < right:
            mid = (left + right) // 2
            # 当前运载能力下需要的天数
            current_days = 1
            current_weight = 0
            
            # 计算在当前运载能力mid下需要多少天
            for weight in weights:
                # 如果加上当前包裹超过运载能力，需要新的一天
                if current_weight + weight > mid:
                    current_days += 1
                    current_weight = 0
                current_weight += weight
            
            # 如果需要的天数小于等于给定天数，说明运载能力足够或偏大
            if current_days <= days:
                right = mid
            else:
                left = mid + 1
        
        return left
