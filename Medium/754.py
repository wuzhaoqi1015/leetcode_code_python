class Solution:
    def reachNumber(self, target: int) -> int:
        # 将目标值转换为正数，因为对称性，正负情况相同
        target = abs(target)
        # 初始化步数和累计和
        step = 0
        total = 0
        # 当累计和小于目标值，或者累计和与目标值的差为奇数时继续循环
        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step
        return step
