class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # 遍历所有可能的a和b值
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # 计算c的平方
                c_square = a * a + b * b
                # 计算c的整数部分
                c = int(c_square ** 0.5)
                # 检查c是否在范围内且满足平方和等式
                if c <= n and c * c == c_square:
                    count += 1
        return count
