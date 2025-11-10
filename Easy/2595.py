class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        idx = 0
        # 遍历二进制位，从最低位开始
        while n:
            # 检查当前位是否为1
            if n & 1:
                # 根据下标奇偶性计数
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            # 右移一位并增加下标
            n >>= 1
            idx += 1
        return [even, odd]
