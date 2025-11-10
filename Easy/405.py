class Solution:
    def toHex(self, num: int) -> str:
        # 处理0的特殊情况
        if num == 0:
            return "0"
        
        # 定义十六进制字符映射
        hex_chars = "0123456789abcdef"
        result = ""
        
        # 处理负数：使用补码表示，通过位运算转换为无符号整数
        # Python中负数使用补码表示，但需要处理为32位无符号整数
        if num < 0:
            num = (1 << 32) + num
        
        # 转换为十六进制
        while num > 0:
            # 取最低4位对应的十六进制字符
            digit = num & 0xf
            result = hex_chars[digit] + result
            # 右移4位
            num >>= 4
            # 对于32位整数，最多处理8次
            if num == 0:
                break
        
        return result
