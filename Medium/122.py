class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化总利润为0
        total_profit = 0
        # 遍历价格数组，从第1个元素到最后一个元素
        for i in range(1, len(prices)):
            # 如果当前价格大于前一天价格，计算利润差并累加
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        # 返回累计的最大利润
        return total_profit
