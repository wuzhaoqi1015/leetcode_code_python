class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 使用栈来存储字符，遇到相同字符则弹出
        stack = []
        for char in s:
            # 如果栈不为空且栈顶元素与当前字符相同，则弹出栈顶
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # 否则将当前字符压入栈中
                stack.append(char)
        # 将栈中剩余字符拼接成字符串返回
        return ''.join(stack)
