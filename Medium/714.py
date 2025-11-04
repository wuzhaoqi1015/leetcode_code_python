class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        # 初始化持有股票和不持有股票的最大利润
        hold = -prices[0]  # 第一天持有股票
        cash = 0           # 第一天不持有股票
        
        for i in range(1, n):
            # 更新持有状态：保持持有或从不持有状态买入
            hold = max(hold, cash - prices[i])
            # 更新不持有状态：保持不持有或从持有状态卖出（扣除手续费）
            cash = max(cash, hold + prices[i] - fee)
            
        return cash
