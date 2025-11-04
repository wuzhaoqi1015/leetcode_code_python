class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base_satisfied = 0
        # 计算不使用技巧时的满意顾客数
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        
        # 计算滑动窗口内因生气而损失的顾客数
        max_extra = 0
        current_extra = 0
        
        # 初始化第一个窗口
        for i in range(minutes):
            if grumpy[i] == 1:
                current_extra += customers[i]
        max_extra = current_extra
        
        # 滑动窗口
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_extra += customers[i]
            if grumpy[i - minutes] == 1:
                current_extra -= customers[i - minutes]
            max_extra = max(max_extra, current_extra)
        
        return base_satisfied + max_extra
