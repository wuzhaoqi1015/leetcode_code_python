class Solution:
    def maximumSwap(self, num: int) -> int:
        # 将数字转换为字符列表便于处理
        digits = list(str(num))
        n = len(digits)
        
        # 记录每个数字最后出现的位置
        last_occurrence = {}
        for i in range(n):
            last_occurrence[int(digits[i])] = i
        
        # 从左到右遍历，找到第一个可以交换的位置
        for i in range(n):
            current_digit = int(digits[i])
            # 从9到当前数字+1，寻找更大的数字
            for d in range(9, current_digit, -1):
                if d in last_occurrence and last_occurrence[d] > i:
                    # 交换数字
                    digits[i], digits[last_occurrence[d]] = digits[last_occurrence[d]], digits[i]
                    # 返回交换后的数字
                    return int(''.join(digits))
        
        # 如果没有交换，返回原数字
        return num
