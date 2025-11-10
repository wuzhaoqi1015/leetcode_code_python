class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 处理特殊情况：n必须为正数且不能为0
        if n <= 0:
            return False
        
        # 检查n是否是2的幂：n & (n-1) == 0
        if n & (n - 1) != 0:
            return False
        
        # 检查n的二进制表示中1的位置是否在奇数位
        # 4的幂的二进制表示中，1的位置总是在奇数位（从右往左数，从1开始）
        # 使用掩码0x55555555来检查（二进制：01010101010101010101010101010101）
        return n & 0x55555555 != 0
