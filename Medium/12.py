class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义罗马数字符号和对应的数值，按从大到小排序
        roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = []  # 用于存储罗马数字字符
        
        # 遍历所有罗马数字符号
        for value, symbol in roman_map:
            # 如果当前数值大于等于当前符号对应的值
            if num >= value:
                # 计算当前符号可以重复的次数
                count = num // value
                # 将符号重复count次添加到结果中
                result.append(symbol * count)
                # 减去已经转换的部分
                num -= value * count
            # 如果num已经为0，提前结束循环
            if num == 0:
                break
        
        # 将结果列表连接成字符串返回
        return ''.join(result)
