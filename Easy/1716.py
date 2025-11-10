class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week_count = n // 7  # 计算完整周数
        remaining_days = n % 7  # 计算剩余天数
        
        # 计算完整周的总存款
        for week in range(week_count):
            base = week + 1  # 当前周的基础存款金额
            total += sum(range(base, base + 7))  # 累加完整周的存款
        
        # 计算剩余天数的存款
        if remaining_days > 0:
            base = week_count + 1  # 剩余天数的基础存款金额
            total += sum(range(base, base + remaining_days))  # 累加剩余天数的存款
        
        return total
