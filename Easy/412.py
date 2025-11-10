class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 初始化结果列表
        result = []
        
        # 遍历从1到n的所有数字
        for i in range(1, n + 1):
            # 同时是3和5的倍数
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # 只是3的倍数
            elif i % 3 == 0:
                result.append("Fizz")
            # 只是5的倍数
            elif i % 5 == 0:
                result.append("Buzz")
            # 其他情况，将数字转为字符串
            else:
                result.append(str(i))
        
        return result
