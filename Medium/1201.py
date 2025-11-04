import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 计算最小公倍数
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        
        # 二分查找
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            # 计算小于等于mid的丑数个数
            count = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left
