class Solution:
    def simplifyPath(self, path: str) -> str:
        # 使用栈来处理路径中的目录
        stack = []
        # 按'/'分割路径，过滤掉空字符串和'.'
        components = [comp for comp in path.split('/') if comp != '' and comp != '.']
        
        # 遍历每个路径组件
        for comp in components:
            if comp == '..':
                # 遇到'..'时，如果栈不为空则弹出栈顶元素（返回上一级目录）
                if stack:
                    stack.pop()
            else:
                # 其他情况（包括'...'等）都视为有效目录名，压入栈中
                stack.append(comp)
        
        # 将栈中的目录组件用'/'连接，并在开头加上'/'
        return '/' + '/'.join(stack)
