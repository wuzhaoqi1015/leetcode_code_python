class Solution:
    def countDigits(self, num: int) -> int:
        # 初始化计数器
        count = 0
        # 将数字转换为字符串以便遍历每一位
        num_str = str(num)
        # 遍历每一位数字
        for digit_char in num_str:
            # 将字符转换为整数
            digit = int(digit_char)
            # 检查当前数字是否能整除原数字
            if digit != 0 and num % digit == 0:
                count += 1
        # 返回满足条件的数字个数
        return count
