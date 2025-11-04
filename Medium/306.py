class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # 遍历所有可能的前两个数字组合
        for i in range(1, n):
            for j in range(i+1, n):
                # 第一个数字
                num1 = num[:i]
                # 第二个数字
                num2 = num[i:j]
                # 检查数字有效性：不能以0开头（除非就是0）
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                # 剩余字符串
                remaining = num[j:]
                # 将前两个数字转为整数
                a = int(num1)
                b = int(num2)
                # 开始验证后续序列
                if self.validate(a, b, remaining):
                    return True
        return False
    
    def validate(self, a: int, b: int, remaining: str) -> bool:
        # 如果没有剩余字符串，说明序列验证完成
        if not remaining:
            return True
        # 计算期望的下一个数字
        expected_sum = a + b
        expected_str = str(expected_sum)
        # 检查剩余字符串是否以期望数字开头
        if not remaining.startswith(expected_str):
            return False
        # 递归验证后续序列
        return self.validate(b, expected_sum, remaining[len(expected_str):])
