class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # 使用栈来存储当前层的字符串
        current = ""  # 当前正在处理的字符串
        
        for char in s:
            if char == '(':
                # 遇到左括号，将当前字符串压入栈，并重置current
                stack.append(current)
                current = ""
            elif char == ')':
                # 遇到右括号，将当前字符串反转，并与栈顶字符串拼接
                current = stack.pop() + current[::-1]
            else:
                # 普通字符，直接添加到当前字符串
                current += char
        
        return current
