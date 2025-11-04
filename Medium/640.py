class Solution:
    def solveEquation(self, equation: str) -> str:
        # 将方程按等号分割为左右两部分
        left_str, right_str = equation.split('=')
        
        # 解析表达式，返回x的系数和常数项
        def parse_expression(expr):
            coeff = 0  # x的系数
            const = 0   # 常数项
            num_str = ''  # 临时存储数字字符串
            sign = 1     # 当前项的符号，1表示正，-1表示负
            has_x = False  # 当前项是否包含x
            
            # 在表达式末尾添加+号，确保处理最后一个项
            expr += '+'
            
            for char in expr:
                if char == '+' or char == '-':
                    # 处理前一个完整的项
                    if num_str or has_x:
                        if has_x:
                            # 处理x项
                            if num_str == '':
                                coeff += sign * 1
                            else:
                                coeff += sign * int(num_str)
                        else:
                            # 处理常数项
                            const += sign * int(num_str)
                    
                    # 重置状态
                    num_str = ''
                    has_x = False
                    sign = 1 if char == '+' else -1
                elif char == 'x':
                    has_x = True
                else:
                    # 数字字符
                    num_str += char
            
            return coeff, const
        
        # 解析左右两边表达式
        left_coeff, left_const = parse_expression(left_str)
        right_coeff, right_const = parse_expression(right_str)
        
        # 将x项移到左边，常数项移到右边
        total_coeff = left_coeff - right_coeff
        total_const = right_const - left_const
        
        # 根据系数和常数项判断解的情况
        if total_coeff == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            # 计算x的值
            x_value = total_const // total_coeff
            # 题目保证解为整数，直接返回
            return f"x={x_value}"
