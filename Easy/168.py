class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # 转换为0-25的范围
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))  # 65是'A'的ASCII码
            columnNumber //= 26
        return ''.join(reversed(result))
