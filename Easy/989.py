class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # 将数组转换为整数
        num_int = 0
        for digit in num:
            num_int = num_int * 10 + digit
        
        # 计算总和
        total = num_int + k
        
        # 处理结果为0的特殊情况
        if total == 0:
            return [0]
        
        # 将总和转换为数组形式
        result = []
        while total > 0:
            result.append(total % 10)
            total //= 10
        
        # 反转数组得到正确顺序
        return result[::-1]
