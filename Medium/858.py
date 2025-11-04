class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # 计算最小公倍数作为光线路径的扩展
        from math import gcd
        lcm = p * q // gcd(p, q)
        # 计算水平和垂直方向的反射次数
        m = lcm // p  # 垂直方向反射次数
        n = lcm // q  # 水平方向反射次数
        # 根据反射次数的奇偶性确定接收器编号
        if m % 2 == 0:
            return 0
        elif n % 2 == 0:
            return 2
        else:
            return 1
