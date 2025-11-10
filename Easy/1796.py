class Solution:
    def secondHighest(self, s: str) -> int:
        # 使用集合存储所有数字字符
        digits = set()
        for char in s:
            if char.isdigit():
                digits.add(char)
        
        # 如果没有数字或只有一个数字，返回-1
        if len(digits) < 2:
            return -1
        
        # 将数字字符转换为整数并排序
        sorted_digits = sorted([int(d) for d in digits], reverse=True)
        
        # 返回第二大的数字
        return sorted_digits[1]
