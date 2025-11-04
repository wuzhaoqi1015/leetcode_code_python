class Solution:
    def soupServings(self, n: int) -> float:
        # 当n很大时，概率趋近于1，直接返回1.0
        if n >= 5000:
            return 1.0
        
        # 将n转换为需要的份数，每份25ml
        m = (n + 24) // 25  # 向上取整
        # 使用记忆化递归，dp[i][j]表示A剩余i份，B剩余j份时的概率
        memo = {}
        
        def dfs(a, b):
            # 如果A先空且B还有剩余，返回1
            if a <= 0 and b > 0:
                return 1.0
            # 如果A和B同时空，返回0.5
            if a <= 0 and b <= 0:
                return 0.5
            # 如果B先空而A还有剩余，返回0
            if b <= 0 and a > 0:
                return 0.0
            
            # 如果已经计算过，直接返回结果
            if (a, b) in memo:
                return memo[(a, b)]
            
            # 四种操作的概率都是0.25
            prob = 0.0
            prob += 0.25 * dfs(a - 4, b)      # 取A 100ml, B 0ml
            prob += 0.25 * dfs(a - 3, b - 1)  # 取A 75ml, B 25ml
            prob += 0.25 * dfs(a - 2, b - 2)  # 取A 50ml, B 50ml
            prob += 0.25 * dfs(a - 1, b - 3)  # 取A 25ml, B 75ml
            
            memo[(a, b)] = prob
            return prob
        
        return dfs(m, m)
