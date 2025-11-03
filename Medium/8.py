class Solution:
    def myAtoi(self, s: str) -> int:
        # 定义32位有符号整数范围
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 初始化索引、符号和结果
        i = 0
        n = len(s)
        sign = 1
        result = 0
        
        # 步骤1：跳过前导空格
        while i < n and s[i] == ' ':
            i += 1
        
        # 如果已经到达字符串末尾，返回0
        if i == n:
            return 0
        
        # 步骤2：检查符号
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 步骤3：转换数字，跳过前置零
        # 先跳过所有前置零
        while i < n and s[i] == '0':
            i += 1
        
        # 开始读取数字
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 检查是否溢出
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # 应用符号并返回结果
        return sign * result
