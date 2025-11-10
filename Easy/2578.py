class Solution:
    def splitNum(self, num: int) -> int:
        # 将数字转换为字符串并排序
        digits = sorted(str(num))
        # 初始化两个数字字符串
        num1 = []
        num2 = []
        # 交替分配数字到两个数
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                num1.append(digit)
            else:
                num2.append(digit)
        # 将列表转换为整数并求和
        return int(''.join(num1)) + int(''.join(num2))
