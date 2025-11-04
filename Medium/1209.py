class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # 使用栈来存储字符及其连续出现次数
        for char in s:
            if stack and stack[-1][0] == char:  # 如果当前字符与栈顶字符相同
                stack[-1][1] += 1  # 增加栈顶字符的计数
                if stack[-1][1] == k:  # 如果达到k个连续相同字符
                    stack.pop()  # 弹出栈顶元素
            else:
                stack.append([char, 1])  # 否则压入新字符，计数为1
        
        # 构建结果字符串
        result = []
        for char, count in stack:
            result.append(char * count)  # 将每个字符重复对应次数
        return ''.join(result)
