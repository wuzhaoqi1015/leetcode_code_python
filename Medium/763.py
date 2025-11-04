class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 记录每个字符最后出现的位置
        last_occurrence = {}
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        
        result = []
        start = 0
        end = 0
        
        # 遍历字符串，确定每个片段的结束位置
        for idx, char in enumerate(s):
            # 更新当前片段的结束位置为当前字符的最后出现位置
            end = max(end, last_occurrence[char])
            
            # 如果当前位置等于当前片段的结束位置
            # 说明找到了一个片段的结束
            if idx == end:
                # 计算当前片段的长度并加入结果
                result.append(end - start + 1)
                # 更新下一个片段的起始位置
                start = idx + 1
        
        return result
