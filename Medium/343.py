class Solution:
    def integerBreak(self, n: int) -> int:
        # 特殊情况处理：当n为2或3时，直接返回对应结果
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # 初始化乘积为1
        product = 1
        # 当n大于4时，不断拆分出3并计算乘积
        while n > 4:
            product *= 3
            n -= 3
        # 最后乘上剩余的n
        product *= n
        return product
