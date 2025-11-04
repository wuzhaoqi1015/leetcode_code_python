class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # 过滤掉不划算的大礼包
        filtered_special = []
        for sp in special:
            # 计算单独购买礼包内物品的总价
            total_price = 0
            for i in range(len(price)):
                total_price += sp[i] * price[i]
            # 只保留价格比单独购买便宜的大礼包
            if total_price > sp[-1]:
                filtered_special.append(sp)
        
        # 使用记忆化搜索
        memo = {}
        
        def dfs(current_needs):
            # 如果当前需求状态已经计算过，直接返回结果
            key = tuple(current_needs)
            if key in memo:
                return memo[key]
            
            # 计算不购买任何礼包，直接按单价购买的总价
            total = 0
            for i in range(len(current_needs)):
                total += current_needs[i] * price[i]
            
            # 尝试每一个大礼包
            for sp in filtered_special:
                # 检查是否可以购买这个大礼包
                new_needs = current_needs.copy()
                valid = True
                
                for i in range(len(current_needs)):
                    # 如果礼包中某物品数量超过当前需求，则不能购买
                    if sp[i] > new_needs[i]:
                        valid = False
                        break
                    new_needs[i] -= sp[i]
                
                # 如果可以购买，递归计算剩余需求的最低价格
                if valid:
                    total = min(total, sp[-1] + dfs(new_needs))
            
            # 记录当前需求状态的最低价格
            memo[key] = total
            return total
        
        return dfs(needs)
