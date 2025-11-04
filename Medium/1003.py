class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈来模拟字符串的构建过程
        stack = []
        for char in s:
            # 如果当前字符是'c'，检查栈顶两个元素是否为'b'和'a'
            if char == 'c':
                # 栈中至少需要有两个元素才能检查
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    # 弹出匹配的'b'和'a'
                    stack.pop()
                    stack.pop()
                else:
                    # 如果不匹配，说明无效
                    return False
            else:
                # 对于'a'和'b'，直接压入栈中
                stack.append(char)
        # 最后栈应该为空才表示有效
        return len(stack) == 0
