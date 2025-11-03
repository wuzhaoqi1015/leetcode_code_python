class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 检查总油量是否足够总消耗，如果不够直接返回-1
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        start = 0  # 起始加油站索引
        current_gas = 0  # 当前油量
        
        for i in range(n):
            # 计算从当前加油站到下一站的净收益
            current_gas += gas[i] - cost[i]
            
            # 如果当前油量小于0，说明从之前起点到当前站不可行
            # 将起点设为下一站，并重置当前油量
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        # 由于题目保证答案唯一，直接返回找到的起点
        return start
