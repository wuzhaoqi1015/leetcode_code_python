class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 特殊情况处理：如果总和小于等于0，先手直接获胜
        if desiredTotal <= 0:
            return True
        # 特殊情况处理：如果所有数字的和都小于目标值，不可能有人获胜
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        # 特殊情况处理：如果所有数字的和等于目标值，根据数字个数的奇偶性决定胜负
        if total_sum == desiredTotal:
            return maxChoosableInteger % 2 == 1
        
        # 使用记忆化递归，状态用位掩码表示
        memo = {}
        
        def dfs(state, current_total):
            # 如果当前状态已经计算过，直接返回结果
            if state in memo:
                return memo[state]
            
            # 遍历所有可选的数字
            for i in range(1, maxChoosableInteger + 1):
                # 检查数字i是否已经被使用
                mask = 1 << (i - 1)
                if state & mask:
                    continue
                
                # 如果选择这个数字后达到或超过目标值，当前玩家获胜
                if current_total + i >= desiredTotal:
                    memo[state] = True
                    return True
                
                # 对手在剩余状态下不能获胜，则当前玩家获胜
                if not dfs(state | mask, current_total + i):
                    memo[state] = True
                    return True
            
            # 所有选择都无法获胜，当前玩家失败
            memo[state] = False
            return False
        
        # 初始状态：没有选择任何数字，当前总和为0
        return dfs(0, 0)
