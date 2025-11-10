class Solution:
    def interpret(self, command: str) -> str:
        result = []  # 使用列表存储解析后的字符，提高拼接效率
        i = 0  # 初始化索引指针
        n = len(command)  # 获取输入字符串长度
        
        while i < n:  # 遍历整个字符串
            if command[i] == 'G':  # 处理'G'字符
                result.append('G')
                i += 1  # 移动到下一个字符
            elif command[i] == '(':  # 遇到左括号，检查后续字符
                if command[i+1] == ')':  # 匹配"()"模式
                    result.append('o')
                    i += 2  # 跳过两个字符
                else:  # 匹配"(al)"模式
                    result.append('al')
                    i += 4  # 跳过四个字符
        
        return ''.join(result)  # 将列表转换为字符串返回
