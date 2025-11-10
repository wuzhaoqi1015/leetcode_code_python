class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 处理特殊情况：n必须为正数，且2的幂次方在二进制表示中只有一个1
        if n <= 0:
            return False
        # 使用位运算：n & (n-1) 会消除最低位的1
        # 如果n是2的幂，那么二进制表示中只有一个1，消除后应该为0
        return (n & (n - 1)) == 0
