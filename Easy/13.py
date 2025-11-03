class Solution:
    def romanToInt(self, s: str) -> int:
        # 创建罗马数字到整数的映射字典
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 遍历字符串中的每个字符
        for i in range(n):
            # 获取当前字符对应的数值
            current_value = roman_map[s[i]]
            
            # 如果当前字符不是最后一个字符，且当前字符的值小于下一个字符的值
            # 则说明是特殊情况（如IV、IX等），需要减去当前值
            if i < n - 1 and current_value < roman_map[s[i + 1]]:
                total -= current_value
            else:
                # 否则正常加上当前值
                total += current_value
                
        return total
