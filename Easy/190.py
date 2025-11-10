class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # 处理32位二进制位
        for i in range(32):
            # 将结果左移一位，为新的最低位腾出空间
            result <<= 1
            # 获取n的最低位，并加到result中
            result |= n & 1
            # 将n右移一位，处理下一个位
            n >>= 1
        return result
