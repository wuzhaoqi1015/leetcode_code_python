# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # 生成1-49的均匀随机数
            num = (rand7() - 1) * 7 + rand7()
            # 如果生成的数在1-40范围内，直接映射到1-10
            if num <= 40:
                return num % 10 + 1
            # 如果生成的数在41-49范围内，利用剩余的值继续生成
            num = (num - 40 - 1) * 7 + rand7()
            # 现在num在1-63范围内
            if num <= 60:
                return num % 10 + 1
            # 如果生成的数在61-63范围内，继续利用剩余的值
            num = (num - 60 - 1) * 7 + rand7()
            # 现在num在1-21范围内
            if num <= 20:
                return num % 10 + 1
