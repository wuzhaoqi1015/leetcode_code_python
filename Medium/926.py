class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 初始化：count_one记录遇到的1的个数，flips记录最小翻转次数
        count_one = 0
        flips = 0
        # 遍历字符串中的每个字符
        for char in s:
            # 如果当前字符是'1'，增加1的计数
            if char == '1':
                count_one += 1
            else:
                # 如果当前字符是'0'，考虑翻转这个0为1或者翻转之前所有的1为0
                # 取翻转当前0和翻转之前所有1的最小值
                flips = min(flips + 1, count_one)
        # 返回最小翻转次数
        return flips
