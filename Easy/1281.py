class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # 初始化乘积为1，和为0
        product = 1
        total_sum = 0
        
        # 将整数转换为字符串，便于逐位处理
        num_str = str(n)
        
        # 遍历每一位数字
        for digit_char in num_str:
            # 将字符转换为整数
            digit = int(digit_char)
            # 更新乘积
            product *= digit
            # 更新和
            total_sum += digit
        
        # 返回乘积与和的差
        return product - total_sum
