class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # 根据公式计算开氏度
        kelvin = celsius + 273.15
        # 根据公式计算华氏度
        fahrenheit = celsius * 1.80 + 32.00
        # 返回结果数组
        return [kelvin, fahrenheit]
