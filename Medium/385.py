class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 如果字符串不以'['开头，说明是单个整数
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = 0
        sign = 1
        has_num = False
        
        for i, char in enumerate(s):
            if char == '-':
                sign = -1
            elif char.isdigit():
                num = num * 10 + int(char)
                has_num = True
            elif char == '[':
                # 遇到左括号，创建新的NestedInteger对象并入栈
                stack.append(NestedInteger())
            elif char == ',' or char == ']':
                # 如果前面有数字，需要添加到当前列表中
                if has_num:
                    # 获取栈顶元素并添加整数
                    stack[-1].add(NestedInteger(sign * num))
                    num = 0
                    sign = 1
                    has_num = False
                
                if char == ']' and len(stack) > 1:
                    # 遇到右括号且栈中有多个元素，弹出当前列表并添加到上一级
                    current = stack.pop()
                    stack[-1].add(current)
        
        return stack[0]
