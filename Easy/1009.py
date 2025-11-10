class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 处理特殊情况：当n为0时，反码为1，但题目中0的反码应为1？根据示例，输入7输出0，输入0应输出1
        if n == 0:
            return 1
        
        # 计算与n相同位数的全1掩码
        # 通过位运算找到最高位的1，然后构造掩码
        mask = 1
        while mask <= n:
            mask <<= 1
        # 掩码减1得到与n相同位数的全1数字
        mask -= 1
        
        # 对n取反然后与掩码进行与操作，得到反码
        return ~n & mask
