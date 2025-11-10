class Solution:
    def minLength(self, s: str) -> int:
        # 使用栈来模拟删除过程
        stack = []
        # 遍历字符串中的每个字符
        for char in s:
            # 如果栈不为空，检查栈顶字符和当前字符是否组成"AB"或"CD"
            if stack:
                # 检查是否组成"AB"
                if stack[-1] == 'A' and char == 'B':
                    stack.pop()  # 删除栈顶的'A'
                    continue     # 跳过当前'B'的入栈
                # 检查是否组成"CD"
                elif stack[-1] == 'C' and char == 'D':
                    stack.pop()  # 删除栈顶的'C'
                    continue     # 跳过当前'D'的入栈
            # 如果不匹配，将当前字符压入栈中
            stack.append(char)
        # 返回栈中剩余字符的数量，即最小可能长度
        return len(stack)
