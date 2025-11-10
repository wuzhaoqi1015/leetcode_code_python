class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 如果总钱数小于儿童数，无法满足每个儿童至少1美元
        if money < children:
            return -1
        
        # 先给每个儿童分配1美元
        money -= children
        
        # 计算最多能有多少个儿童获得额外的7美元（即总共8美元）
        count = min(money // 7, children)
        money -= count * 7
        
        # 检查剩余情况
        # 如果所有儿童都分配了8美元但还有钱剩余，需要调整
        if count == children and money > 0:
            return children - 1
        
        # 如果最后一个获得8美元的儿童因为剩余4美元而违反规则
        if count == children - 1 and money == 3:
            return children - 2
        
        return count
