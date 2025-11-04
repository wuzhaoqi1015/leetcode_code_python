class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # 如果目标水量大于两个水壶的总容量，则不可能实现
        if target > x + y:
            return False
        # 如果目标水量为0，则已经满足条件
        if target == 0:
            return True
        # 使用欧几里得算法计算最大公约数
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        # 检查目标水量是否是两个水壶容量的最大公约数的倍数
        g = gcd(x, y)
        return target % g == 0
