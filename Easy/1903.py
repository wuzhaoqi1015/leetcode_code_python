class Solution:
    def largestOddNumber(self, num: str) -> str:
        # 从右向左遍历，找到第一个奇数数字的位置
        for i in range(len(num) - 1, -1, -1):
            # 检查当前数字是否为奇数
            if int(num[i]) % 2 == 1:
                # 返回从开头到该位置的子字符串
                return num[:i+1]
        # 如果没有找到奇数，返回空字符串
        return ""
