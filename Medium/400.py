class Solution:
    def findNthDigit(self, n: int) -> int:
        # 定义数字位数和该位数下的数字个数
        digit = 1  # 当前数字的位数
        start = 1  # 当前位数数字的起始值
        count = 9  # 当前位数数字的总个数
        
        # 确定n所在的数字位数
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = 9 * start * digit
        
        # 确定n所在的数字
        num = start + (n - 1) // digit
        
        # 确定数字中的具体位
        return int(str(num)[(n - 1) % digit])
