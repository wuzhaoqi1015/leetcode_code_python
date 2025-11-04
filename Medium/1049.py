class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 计算所有石头的总重量
        total = sum(stones)
        # 目标是将石头分成两堆，使得两堆重量差最小
        # 问题转化为背包容量为total//2时能装的最大重量
        target = total // 2
        # 创建动态规划数组，dp[j]表示容量为j的背包能装的最大重量
        dp = [0] * (target + 1)
        
        # 遍历每个石头
        for stone in stones:
            # 从后往前遍历，避免重复使用同一块石头
            for j in range(target, stone - 1, -1):
                # 更新dp数组，选择是否放入当前石头
                dp[j] = max(dp[j], dp[j - stone] + stone)
        
        # 最终结果为总重量减去两倍dp[target]，即两堆石头的重量差
        return total - 2 * dp[target]
