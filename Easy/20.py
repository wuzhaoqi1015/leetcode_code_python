class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈来匹配括号
        stack = []
        # 定义括号映射关系
        mapping = {')': '(', '}': '{', ']': '['}
        
        # 遍历字符串中的每个字符
        for char in s:
            if char in mapping:
                # 如果是右括号，检查栈顶元素是否匹配
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()  # 匹配成功，弹出栈顶元素
            else:
                # 如果是左括号，压入栈中
                stack.append(char)
        
        # 最后检查栈是否为空
        return not stack
