class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 使用动态规划，dp[i]表示到第i天为止的最小花费
        # 初始化dp数组，长度为最后一天+1，初始值设为0
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        
        # 将需要旅行的天数转换为集合，便于快速查找
        travel_days = set(days)
        
        # 从第1天开始遍历到最后一天
        for i in range(1, last_day + 1):
            if i not in travel_days:
                # 如果当天不需要旅行，花费与前一天相同
                dp[i] = dp[i - 1]
            else:
                # 如果当天需要旅行，考虑三种购票方案的最小值
                # 方案1：购买1天票
                cost1 = dp[i - 1] + costs[0]
                
                # 方案2：购买7天票（如果i-7<0，则从第0天开始）
                cost2 = dp[max(0, i - 7)] + costs[1]
                
                # 方案3：购买30天票（如果i-30<0，则从第0天开始）
                cost3 = dp[max(0, i - 30)] + costs[2]
                
                # 取三种方案的最小值
                dp[i] = min(cost1, cost2, cost3)
        
        return dp[last_day]
