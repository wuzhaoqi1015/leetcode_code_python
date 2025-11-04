class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # 移除输入字符串的首尾括号
        s = s[1:-1]
        n = len(s)
        res = []
        
        # 遍历所有可能的分割点
        for i in range(1, n):
            left = s[:i]  # 第一个数字部分
            right = s[i:]  # 第二个数字部分
            
            # 生成左半部分所有可能的有效数字表示
            left_list = self.generate_valid_numbers(left)
            # 生成右半部分所有可能的有效数字表示
            right_list = self.generate_valid_numbers(right)
            
            # 组合所有可能的坐标对
            for l in left_list:
                for r in right_list:
                    res.append(f"({l}, {r})")
        
        return res
    
    def generate_valid_numbers(self, num_str: str) -> List[str]:
        # 如果字符串长度为1，直接返回
        if len(num_str) == 1:
            return [num_str]
        
        result = []
        
        # 情况1：不加小数点
        if self.is_valid_integer(num_str):
            result.append(num_str)
        
        # 情况2：在每一个可能的位置加小数点
        for i in range(1, len(num_str)):
            integer_part = num_str[:i]
            decimal_part = num_str[i:]
            
            # 检查整数部分和小数部分是否都有效
            if self.is_valid_integer(integer_part) and self.is_valid_decimal(decimal_part):
                result.append(f"{integer_part}.{decimal_part}")
        
        return result
    
    def is_valid_integer(self, s: str) -> bool:
        # 整数不能以0开头，除非它就是"0"
        if len(s) > 1 and s[0] == '0':
            return False
        return True
    
    def is_valid_decimal(self, s: str) -> bool:
        # 小数部分不能以0结尾
        if s[-1] == '0':
            return False
        return True
