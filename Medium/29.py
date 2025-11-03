class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 处理特殊情况：被除数为0，直接返回0
        if dividend == 0:
            return 0
            
        # 处理特殊情况：除数为1，直接返回被除数
        if divisor == 1:
            return self.handle_overflow(dividend)
            
        # 处理特殊情况：除数为-1，返回被除数的相反数
        if divisor == -1:
            return self.handle_overflow(-dividend)
        
        # 确定结果的符号
        negative = (dividend < 0) != (divisor < 0)
        
        # 将被除数和除数都转换为正数处理
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        # 使用位运算进行除法计算
        while a >= b:
            temp = b
            multiple = 1
            
            # 找到最大的倍数，使得 temp * 2 <= a
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            # 减去这个倍数对应的值
            a -= temp
            result += multiple
        
        # 根据符号调整结果
        if negative:
            result = -result
            
        return self.handle_overflow(result)
    
    def handle_overflow(self, value: int) -> int:
        """处理整数溢出问题"""
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if value > INT_MAX:
            return INT_MAX
        elif value < INT_MIN:
            return INT_MIN
        else:
            return value
