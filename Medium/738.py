class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将数字转换为字符串列表，便于逐位处理
        digits = list(str(n))
        length = len(digits)
        
        # 从右向左遍历，找到第一个不满足单调递增的位置
        pos = length  # 记录需要调整的位置
        for i in range(length - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                pos = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)
        
        # 将pos位置及之后的所有位设置为9
        for i in range(pos, length):
            digits[i] = '9'
        
        # 将列表转换回整数并返回
        return int(''.join(digits))
