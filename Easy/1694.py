class Solution:
    def reformatNumber(self, number: str) -> str:
        # 首先删除所有非数字字符
        digits = ''.join(c for c in number if c.isdigit())
        n = len(digits)
        result = []
        i = 0
        
        # 处理前面的3个数字一组
        while i < n - 4:
            result.append(digits[i:i+3])
            i += 3
        
        # 处理最后4个或更少的数字
        remaining = n - i
        if remaining == 4:
            result.append(digits[i:i+2])
            result.append(digits[i+2:i+4])
        elif remaining == 3:
            result.append(digits[i:i+3])
        elif remaining == 2:
            result.append(digits[i:i+2])
        
        # 用破折号连接所有块
        return '-'.join(result)
