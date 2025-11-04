class Solution:
    def originalDigits(self, s: str) -> str:
        # 统计输入字符串中每个字符的出现次数
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # 初始化数字计数数组
        digit_count = [0] * 10
        
        # 根据唯一特征字符依次识别数字
        # zero: 只有z是唯一的
        digit_count[0] = char_count.get('z', 0)
        # two: 只有w是唯一的
        digit_count[2] = char_count.get('w', 0)
        # four: 只有u是唯一的
        digit_count[4] = char_count.get('u', 0)
        # six: 只有x是唯一的
        digit_count[6] = char_count.get('x', 0)
        # eight: 只有g是唯一的
        digit_count[8] = char_count.get('g', 0)
        
        # three: 在去掉two和eight后，h只出现在three中
        digit_count[3] = char_count.get('h', 0) - digit_count[8]
        # five: 在去掉four后，f只出现在five中
        digit_count[5] = char_count.get('f', 0) - digit_count[4]
        # seven: 在去掉six后，s只出现在seven中
        digit_count[7] = char_count.get('s', 0) - digit_count[6]
        
        # one: 在去掉zero、two、four后，o只出现在one中
        digit_count[1] = char_count.get('o', 0) - digit_count[0] - digit_count[2] - digit_count[4]
        # nine: 在去掉five、six、eight后，i只出现在nine中
        digit_count[9] = char_count.get('i', 0) - digit_count[5] - digit_count[6] - digit_count[8]
        
        # 构建结果字符串
        result = []
        for digit in range(10):
            result.append(str(digit) * digit_count[digit])
        
        return ''.join(result)
