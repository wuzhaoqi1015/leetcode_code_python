class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 初始化结果变量
        result = 0
        # 遍历字符串中的每个字符
        for char in columnTitle:
            # 将当前字符转换为对应的数值（A=1, B=2, ..., Z=26）
            # 通过计算字符与'A'的ASCII码差值并加1得到
            current_value = ord(char) - ord('A') + 1
            # 将结果乘以26（相当于26进制）并加上当前字符的值
            result = result * 26 + current_value
        # 返回最终计算结果
        return result
