class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math
        # 初始化分子和分母
        numerator = 0
        denominator = 1
        i = 0
        n = len(expression)
        
        while i < n:
            # 读取符号
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            # 读取分子
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num *= sign
            
            # 跳过'/'
            i += 1
            
            # 读取分母
            den = 0
            while i < n and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1
            
            # 计算当前分数与累加结果的和
            numerator = numerator * den + num * denominator
            denominator *= den
            
            # 约分
            gcd_val = math.gcd(abs(numerator), denominator)
            numerator //= gcd_val
            denominator //= gcd_val
        
        # 返回最简分数形式
        return f"{numerator}/{denominator}"
