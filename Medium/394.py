class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 使用栈来处理嵌套的编码字符串
        current_str = ""  # 当前正在处理的字符串
        current_num = 0  # 当前解析的数字
        
        for char in s:
            if char.isdigit():  # 如果是数字字符
                current_num = current_num * 10 + int(char)  # 构建多位数
            elif char == '[':  # 遇到左括号，将当前状态压入栈
                stack.append((current_str, current_num))  # 保存当前字符串和重复次数
                current_str = ""  # 重置当前字符串
                current_num = 0  # 重置当前数字
            elif char == ']':  # 遇到右括号，处理解码
                prev_str, num = stack.pop()  # 弹出栈顶元素
                current_str = prev_str + current_str * num  # 解码当前字符串
            else:  # 普通字母字符
                current_str += char  # 直接添加到当前字符串
        
        return current_str  # 返回最终解码结果
