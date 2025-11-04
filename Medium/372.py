class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # 定义模数
        MOD = 1337
        
        # 使用快速幂算法计算 a^k mod MOD
        def quick_pow(base, exponent):
            result = 1
            base %= MOD
            while exponent > 0:
                if exponent & 1:  # 如果指数是奇数
                    result = (result * base) % MOD
                base = (base * base) % MOD  # 底数平方
                exponent >>= 1  # 指数右移一位（除以2）
            return result
        
        # 处理特殊情况：a为1时，任何次幂都是1
        if a % MOD == 1:
            return 1
        
        # 将数组b表示的整数转换为实际数值
        n = len(b)
        result = 1
        
        # 使用欧拉定理：a^φ(1337) ≡ 1 mod 1337
        # 1337 = 7 * 191，φ(1337) = 1337 * (1-1/7) * (1-1/191) = 1140
        # 所以我们可以对指数取模1140来简化计算
        
        # 计算指数对1140取模的值
        exponent = 0
        for digit in b:
            exponent = (exponent * 10 + digit) % 1140
        
        # 如果指数为0，根据欧拉定理，结果应该是1
        # 但需要注意特殊情况：当指数为0且a不为0时，a^0 = 1
        if exponent == 0:
            exponent = 1140  # 根据欧拉定理，a^1140 ≡ 1 mod 1337
        
        # 使用快速幂计算 a^exponent mod 1337
        return quick_pow(a, exponent)
