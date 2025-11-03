class Solution:
    def reverse(self, x: int) -> int:
        # 定义32位整数范围
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # 处理负数情况，记录符号并转为正数处理
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        # 反转数字
        reversed_num = 0
        while x_abs > 0:
            # 获取最后一位数字
            digit = x_abs % 10
            # 检查反转后的数字是否会超出32位整数范围
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            # 构建反转后的数字
            reversed_num = reversed_num * 10 + digit
            # 移除已处理的最低位
            x_abs //= 10
        
        # 应用符号并返回结果
        result = sign * reversed_num
        return result
