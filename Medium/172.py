class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 尾随零的数量由因子2和因子5的个数决定，由于因子2总是比因子5多，因此只需计算因子5的个数
        count = 0
        # 遍历所有5的幂次
        while n > 0:
            n //= 5
            count += n
        return count
