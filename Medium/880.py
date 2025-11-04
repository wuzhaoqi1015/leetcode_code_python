class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # 计算解码字符串的总长度
        total_length = 0
        
        # 第一次遍历：计算总长度直到达到或超过k
        for char in s:
            if char.isdigit():
                # 遇到数字，将当前长度乘以数字值
                total_length *= int(char)
            else:
                # 遇到字母，长度加1
                total_length += 1
        
        # 第二次遍历：从后向前回溯找到第k个字符
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            k %= total_length  # 关键步骤：通过取模缩小k的范围
            
            # 如果k为0且当前字符是字母，则找到目标字符
            if k == 0 and char.isalpha():
                return char
            
            # 调整总长度
            if char.isdigit():
                # 遇到数字，将总长度除以数字值
                total_length //= int(char)
            else:
                # 遇到字母，总长度减1
                total_length -= 1
        
        return ""  # 理论上不会执行到这里
