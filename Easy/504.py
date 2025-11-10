class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_negative = num < 0
        num = abs(num)
        
        result = []
        while num > 0:
            remainder = num % 7
            result.append(str(remainder))
            num //= 7
        
        result_str = ''.join(result[::-1])
        
        if is_negative:
            result_str = '-' + result_str
            
        return result_str
