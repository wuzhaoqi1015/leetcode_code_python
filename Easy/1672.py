class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # 初始化最大财富值为0
        max_wealth = 0
        
        # 遍历每个客户的账户
        for customer in accounts:
            # 计算当前客户的总资产
            current_wealth = sum(customer)
            # 更新最大财富值
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        
        # 返回最大财富值
        return max_wealth
