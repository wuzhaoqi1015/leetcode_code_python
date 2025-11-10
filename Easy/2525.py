class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # 检查是否为Bulky：至少一个维度 >= 10000 或体积 >= 10^9
        bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4 or 
                length * width * height >= 10**9)
        # 检查是否为Heavy：质量 >= 100
        heavy = mass >= 100
        
        # 根据条件组合返回对应类别
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"
