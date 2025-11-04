class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 计算每个人去A市和去B市的费用差，并按差值排序
        # 费用差 = cost_A - cost_B，这样排序后前面的人更适合去A市，后面的人更适合去B市
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_cost = 0
        
        # 前n个人去A市
        for i in range(n):
            total_cost += sorted_costs[i][0]
        
        # 后n个人去B市
        for i in range(n, 2 * n):
            total_cost += sorted_costs[i][1]
        
        return total_cost
