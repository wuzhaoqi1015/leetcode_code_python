class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 处理n为负数的情况，转换为正数计算后取倒数
        if n < 0:
            x = 1 / x
            n = -n
        
        # 快速幂算法
        def fast_power(base, exponent):
            if exponent == 0:
                return 1.0
            # 递归计算一半的幂次
            half = fast_power(base, exponent // 2)
            # 如果指数是偶数，结果为half的平方
            if exponent % 2 == 0:
                return half * half
            # 如果指数是奇数，结果为half的平方再乘以base
            else:
                return half * half * base
        
        return fast_power(x, n)
