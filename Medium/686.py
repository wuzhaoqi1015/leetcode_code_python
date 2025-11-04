class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 如果b是空字符串，返回0
        if not b:
            return 0
        # 如果a已经包含b，直接返回1
        if b in a:
            return 1
        
        # 计算需要的最小重复次数
        # 最少需要ceil(len(b)/len(a))次，最多需要ceil(len(b)/len(a)) + 2次
        min_repeat = (len(b) + len(a) - 1) // len(a)
        repeated = a * min_repeat
        
        # 检查当前重复次数是否包含b
        if b in repeated:
            return min_repeat
        
        # 再增加一次重复，检查是否包含b
        repeated += a
        if b in repeated:
            return min_repeat + 1
        
        # 再增加一次重复，检查是否包含b
        repeated += a
        if b in repeated:
            return min_repeat + 2
        
        # 如果都不包含，返回-1
        return -1
