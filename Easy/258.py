class Solution:
    def addDigits(self, num: int) -> int:
        # 直接使用数学公式：数字根等于 num 对 9 取模，当 num 能被 9 整除且不为 0 时结果为 9
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
