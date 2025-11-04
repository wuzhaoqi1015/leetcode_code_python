class Solution:
    def numSteps(self, s: str) -> int:
        # 将二进制字符串转换为整数
        num = int(s, 2)
        steps = 0
        # 当数字大于1时循环执行操作
        while num > 1:
            # 如果是偶数，除以2
            if num % 2 == 0:
                num //= 2
            # 如果是奇数，加1
            else:
                num += 1
            steps += 1
        return steps
