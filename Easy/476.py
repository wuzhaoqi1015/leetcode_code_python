class Solution:
    def findComplement(self, num: int) -> int:
        # 计算与num二进制位数相同的全1掩码
        mask = 1
        while mask < num:
            mask = (mask << 1) | 1
        # 将num与掩码进行异或操作得到补数
        return num ^ mask
