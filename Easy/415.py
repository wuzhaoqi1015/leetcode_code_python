class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 初始化指针和进位
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        
        # 从右往左逐位相加
        while i >= 0 or j >= 0 or carry:
            # 获取当前位的数字，如果指针越界则用0代替
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # 计算当前位的和
            total = digit1 + digit2 + carry
            # 计算当前位的值
            current_digit = total % 10
            # 计算进位
            carry = total // 10
            
            # 将当前位加入结果列表
            result.append(str(current_digit))
            
            # 移动指针
            i -= 1
            j -= 1
        
        # 由于是从低位到高位添加的，需要反转得到正确顺序
        return ''.join(result[::-1])
