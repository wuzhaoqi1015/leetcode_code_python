class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 将整数转换为字符列表以便处理
        digits = list(str(n))
        length = len(digits)
        
        # 从右向左找到第一个降序的位置
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # 如果没有找到降序位置，说明已经是最大排列，返回-1
        if i == -1:
            return -1
            
        # 从右向左找到第一个大于digits[i]的数字
        j = length - 1
        while j > i and digits[j] <= digits[i]:
            j -= 1
            
        # 交换这两个数字
        digits[i], digits[j] = digits[j], digits[i]
        
        # 将i之后的部分反转，使其成为最小序列
        left, right = i + 1, length - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
            
        # 将字符列表转换回整数
        result = int(''.join(digits))
        
        # 检查结果是否在32位整数范围内
        if result > 2**31 - 1:
            return -1
            
        return result
