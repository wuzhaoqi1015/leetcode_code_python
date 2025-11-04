class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 使用位运算实现加法
        # 32位整数范围
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        # 循环直到没有进位
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 计算无进位和
            a = (a ^ b) & MASK
            # 将进位赋值给b，继续下一轮计算
            b = carry & MASK
        
        # 处理负数情况
        if a > MAX_INT:
            a = ~(a ^ MASK)
        
        return a
