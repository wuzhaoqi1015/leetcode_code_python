class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        # 处理符号
        sign = ""
        if (numerator < 0) ^ (denominator < 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # 整数部分
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            return sign + str(integer_part)
        
        # 小数部分
        decimal_part = []
        remainder_map = {}
        index = 0
        
        while remainder != 0:
            if remainder in remainder_map:
                # 发现循环节
                start_index = remainder_map[remainder]
                non_repeating = "".join(decimal_part[:start_index])
                repeating = "".join(decimal_part[start_index:])
                return sign + str(integer_part) + "." + non_repeating + "(" + repeating + ")"
            
            remainder_map[remainder] = index
            remainder *= 10
            decimal_digit = remainder // denominator
            decimal_part.append(str(decimal_digit))
            remainder = remainder % denominator
            index += 1
        
        # 有限小数
        return sign + str(integer_part) + "." + "".join(decimal_part)
