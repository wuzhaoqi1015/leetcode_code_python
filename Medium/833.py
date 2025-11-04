class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # 创建一个列表来记录每个位置是否需要替换以及替换的目标
        replace_info = [None] * len(s)
        
        # 遍历所有替换操作
        for i in range(len(indices)):
            idx = indices[i]
            source = sources[i]
            target = targets[i]
            
            # 检查子字符串是否匹配
            if s[idx:idx+len(source)] == source:
                # 标记需要替换的位置
                replace_info[idx] = (len(source), target)
        
        # 构建结果字符串
        result = []
        i = 0
        while i < len(s):
            if replace_info[i] is not None:
                # 执行替换
                source_len, target = replace_info[i]
                result.append(target)
                i += source_len
            else:
                # 保留原字符
                result.append(s[i])
                i += 1
        
        return ''.join(result)
