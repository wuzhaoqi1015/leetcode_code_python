# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n  # 初始化搜索范围为1到n
        while left <= right:  # 当左边界不超过右边界时循环
            mid = left + (right - left) // 2  # 计算中间值，避免整数溢出
            res = guess(mid)  # 调用guess接口获取猜测结果
            if res == 0:  # 如果猜对了
                return mid  # 返回正确的数字
            elif res == -1:  # 如果猜测的数字太大
                right = mid - 1  # 调整右边界
            else:  # 如果猜测的数字太小
                left = mid + 1  # 调整左边界
        return -1  # 理论上不会执行到这里，因为数字一定在范围内
