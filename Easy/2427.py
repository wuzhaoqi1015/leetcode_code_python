class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # 计算a和b的最大公约数
        gcd_val = self.gcd(a, b)
        count = 0
        
        # 遍历从1到最大公约数的所有数
        for i in range(1, gcd_val + 1):
            # 如果i能整除最大公约数，则i是公因子
            if gcd_val % i == 0:
                count += 1
                
        return count
    
    def gcd(self, a: int, b: int) -> int:
        # 使用欧几里得算法计算最大公约数
        while b:
            a, b = b, a % b
        return a
