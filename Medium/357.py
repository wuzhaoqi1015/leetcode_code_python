class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 处理n=0的特殊情况
        if n == 0:
            return 1
        
        # 初始化结果，包含0-9这10个数字
        result = 10
        # 当前位数的可选数字个数，初始为9（1-9，因为首位不能为0）
        available_digits = 9
        # 当前位数的乘积，用于计算不同位数的唯一数字个数
        current_product = 9
        
        # 从2位数开始计算到n位数
        for i in range(2, n + 1):
            # 计算当前位数的唯一数字个数
            current_product *= available_digits
            # 累加到结果中
            result += current_product
            # 可用数字减少1（因为每增加一位，可用的不同数字就少一个）
            available_digits -= 1
            # 如果可用数字为0，提前结束循环
            if available_digits == 0:
                break
        
        return result
