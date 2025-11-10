class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # 将整数转换为字符串以便逐个处理数字
        num_str = str(n)
        total = 0
        # 遍历每个数字，根据位置决定符号
        for i, char in enumerate(num_str):
            digit = int(char)
            # 偶数索引（包括0）为正，奇数索引为负
            if i % 2 == 0:
                total += digit
            else:
                total -= digit
        return total
