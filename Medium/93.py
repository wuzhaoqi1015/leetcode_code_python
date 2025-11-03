class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        
        # 回溯函数，i表示当前处理到的字符索引，segments存储当前已分割的段
        def backtrack(start, segments):
            # 如果已经分割出4段且处理完所有字符，则找到一个有效IP
            if len(segments) == 4:
                if start == n:
                    result.append('.'.join(segments))
                return
            
            # 尝试从当前位置开始取1-3个字符作为一个段
            for length in range(1, 4):
                # 确保不会越界
                if start + length > n:
                    break
                
                segment = s[start:start+length]
                
                # 检查段的合法性：不能有前导0（除非段就是"0"），且数值在0-255之间
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                
                # 当前段合法，加入segments并继续递归
                segments.append(segment)
                backtrack(start + length, segments)
                segments.pop()  # 回溯
        
        backtrack(0, [])
        return result
