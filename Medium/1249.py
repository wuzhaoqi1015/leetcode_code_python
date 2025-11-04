class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 使用栈来跟踪未匹配的左括号索引
        stack = []
        # 将字符串转换为列表以便修改
        s_list = list(s)
        
        # 第一遍遍历：标记需要删除的右括号
        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)  # 记录左括号位置
            elif char == ')':
                if stack:
                    stack.pop()  # 有匹配的左括号，弹出
                else:
                    s_list[i] = ''  # 没有匹配的左括号，标记删除
        
        # 第二遍处理：标记栈中剩余未匹配的左括号
        while stack:
            s_list[stack.pop()] = ''  # 标记未匹配的左括号为删除
        
        # 连接剩余字符形成结果字符串
        return ''.join(s_list)
