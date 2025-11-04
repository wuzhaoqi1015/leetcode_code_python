class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # 解析第一个复数字符串，提取实部和虚部
        real1, imag1 = num1.split('+')
        imag1 = imag1[:-1]  # 去掉末尾的'i'
        
        # 解析第二个复数字符串，提取实部和虚部
        real2, imag2 = num2.split('+')
        imag2 = imag2[:-1]  # 去掉末尾的'i'
        
        # 将字符串转换为整数
        a = int(real1)
        b = int(imag1)
        c = int(real2)
        d = int(imag2)
        
        # 计算复数乘法的实部和虚部
        # (a+bi)(c+di) = ac + adi + bci + bdi²
        # 由于 i² = -1，所以 = (ac - bd) + (ad + bc)i
        real_part = a * c - b * d
        imag_part = a * d + b * c
        
        # 格式化输出结果
        return f"{real_part}+{imag_part}i"
