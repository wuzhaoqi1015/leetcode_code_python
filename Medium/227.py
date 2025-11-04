class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'  # 初始化操作符为'+'
        s = s.replace(' ', '')  # 去除所有空格
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)  # 构建完整数字
            if not char.isdigit() or i == len(s) - 1:  # 遇到操作符或字符串结尾
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)  # 立即计算乘法
                elif sign == '/':
                    # 整数除法，向零取整
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(abs(prev) // num))
                    else:
                        stack.append(prev // num)
                sign = char  # 更新操作符
                num = 0  # 重置数字
        return sum(stack)  # 返回栈中所有数字的和
