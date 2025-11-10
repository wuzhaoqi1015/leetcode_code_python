# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2  # 防止整数溢出
            if isBadVersion(mid):
                right = mid  # 第一个错误版本在左半部分
            else:
                left = mid + 1  # 第一个错误版本在右半部分
        return left  # 此时left和right相等，指向第一个错误版本
