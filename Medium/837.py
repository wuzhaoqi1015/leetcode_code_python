class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 如果k为0，游戏不会进行，分数始终为0，不超过n的概率为1
        if k == 0:
            return 1.0
        # dp[i]表示从i分开始游戏，最终得分不超过n的概率
        dp = [0.0] * (k + maxPts)
        # 当分数在[k, min(n, k+maxPts-1)]范围内时，停止抽牌且分数不超过n，概率为1
        for i in range(k, min(n, k + maxPts - 1) + 1):
            dp[i] = 1.0
        # 当分数在[min(n, k+maxPts-1)+1, k+maxPts-1]范围内时，停止抽牌但分数超过n，概率为0
        # 初始化dp[k-1]：从k-1分开始，下一张牌可能得到1到maxPts分
        # 使用滑动窗口计算概率和，避免重复计算
        window_sum = sum(dp[k:k+maxPts])
        for i in range(k-1, -1, -1):
            dp[i] = window_sum / maxPts
            # 更新窗口和，移除右端元素，加入左端元素
            if i + maxPts < len(dp):
                window_sum += dp[i] - dp[i + maxPts]
        return dp[0]
