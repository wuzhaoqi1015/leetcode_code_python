class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            # 计算当前攻击和下一次攻击之间的间隔
            gap = timeSeries[i + 1] - timeSeries[i]
            # 如果间隔小于持续时间，只累加间隔时间，否则累加完整的持续时间
            total += min(gap, duration)
        # 最后一次攻击会持续完整的持续时间
        total += duration
        return total
