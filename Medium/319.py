class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 灯泡开关状态变化的次数等于其编号的因子个数
        # 只有因子个数为奇数的灯泡最终会亮着
        # 完全平方数的因子个数为奇数
        # 因此问题转化为求1到n中完全平方数的个数
        return int(n ** 0.5)
