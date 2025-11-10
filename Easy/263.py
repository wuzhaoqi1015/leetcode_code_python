class Solution:
    def isUgly(self, n: int) -> bool:
        # 处理特殊情况：非正数直接返回False
        if n <= 0:
            return False
        
        # 不断除以2，直到不能被2整除
        while n % 2 == 0:
            n //= 2
        
        # 不断除以3，直到不能被3整除
        while n % 3 == 0:
            n //= 3
        
        # 不断除以5，直到不能被5整除
        while n % 5 == 0:
            n //= 5
        
        # 如果最终结果为1，说明只包含2、3、5质因数
        return n == 1
