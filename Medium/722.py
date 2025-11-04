class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False  # 标记是否在块注释中
        result = []  # 存储最终结果
        new_line = []  # 存储当前正在构建的新行
        
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not in_block:
                    # 不在块注释中，检查可能的注释开始
                    if i + 1 < n and line[i:i+2] == '/*':
                        in_block = True
                        i += 1  # 跳过'*'，下次循环从'/'后开始
                    elif i + 1 < n and line[i:i+2] == '//':
                        break  # 行注释，忽略该行剩余部分
                    else:
                        new_line.append(line[i])  # 普通字符，添加到新行
                else:
                    # 在块注释中，寻找注释结束
                    if i + 1 < n and line[i:i+2] == '*/':
                        in_block = False
                        i += 1  # 跳过'/'，下次循环从'*'后开始
                i += 1
            
            # 如果不在块注释中且新行不为空，添加到结果
            if not in_block and new_line:
                result.append(''.join(new_line))
                new_line = []  # 重置新行
        
        return result
