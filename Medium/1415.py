class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 使用回溯法生成所有有效的开心字符串
        result = []
        chars = ['a', 'b', 'c']
        
        def backtrack(current):
            # 如果当前字符串长度达到n，加入结果列表
            if len(current) == n:
                result.append(current)
                return
            # 遍历所有可能的字符
            for c in chars:
                # 如果当前字符串为空，或者最后一个字符不等于当前字符
                if not current or current[-1] != c:
                    backtrack(current + c)
                    # 如果结果数量已经达到k，提前终止
                    if len(result) >= k:
                        return
        
        backtrack("")
        # 如果结果数量小于k，返回空字符串
        if len(result) < k:
            return ""
        # 返回第k个字符串（索引为k-1）
        return result[k-1]
