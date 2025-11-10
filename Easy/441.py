class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 使用二分查找法找到最大的k使得k*(k+1)//2 <= n
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        # 当循环结束时，right是满足条件的最大整数
        return right
