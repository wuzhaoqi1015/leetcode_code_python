class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 使用二分查找法在[1, num]范围内查找平方根
        if num < 1:
            return False
        if num == 1:
            return True
            
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
