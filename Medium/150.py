class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # 使用栈来存储操作数
        operators = {'+', '-', '*', '/'}  # 定义有效的运算符集合
        
        for token in tokens:
            if token not in operators:  # 如果是数字，直接入栈
                stack.append(int(token))
            else:  # 如果是运算符，从栈中弹出两个操作数进行运算
                num2 = stack.pop()  # 第二个操作数
                num1 = stack.pop()  # 第一个操作数
                
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    # 使用整数除法，向零截断
                    result = int(num1 / num2)
                
                stack.append(result)  # 将计算结果压回栈中
        
        return stack[0]  # 栈中最后剩下的就是最终结果
