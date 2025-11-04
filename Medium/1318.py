class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # 初始化翻转次数
        flips = 0
        # 遍历每个比特位，最多31位（因为10^9 < 2^30）
        for i in range(31):
            # 获取a、b、c当前比特位的值
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            
            # 如果c的当前位为1
            if bit_c == 1:
                # 需要a或b至少有一个为1，否则需要翻转一次
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            # 如果c的当前位为0
            else:
                # 需要a和b都为0，否则需要翻转
                if bit_a == 1:
                    flips += 1
                if bit_b == 1:
                    flips += 1
        return flips
