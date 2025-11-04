class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # 使用栈来维护当前路径的层级结构
        stack = []
        max_length = 0
        # 按换行符分割输入字符串
        lines = input.split('\n')
        
        for line in lines:
            # 计算当前行的缩进级别（制表符数量）
            level = line.count('\t')
            # 移除制表符得到实际名称
            name = line.replace('\t', '')
            
            # 如果栈中元素数量大于当前层级，弹出多余元素
            while len(stack) > level:
                stack.pop()
            
            # 计算当前路径长度
            if stack:
                # 当前路径长度 = 父路径长度 + '/' + 当前名称长度
                current_length = stack[-1] + len(name) + 1
            else:
                # 根目录情况
                current_length = len(name)
            
            # 将当前路径长度压入栈
            stack.append(current_length)
            
            # 如果是文件（包含扩展名），更新最大长度
            if '.' in name:
                max_length = max(max_length, current_length)
        
        return max_length
