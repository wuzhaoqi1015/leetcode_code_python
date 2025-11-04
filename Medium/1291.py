class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        # 遍历所有可能的数字长度，从2位到9位
        for length in range(2, 10):
            # 遍历所有可能的起始数字
            for start in range(1, 10 - length + 1):
                # 构建顺次数
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                # 检查是否在范围内
                if low <= num <= high:
                    result.append(num)
                # 如果超出上限，提前结束
                elif num > high:
                    break
        # 按升序排序结果
        result.sort()
        return result
