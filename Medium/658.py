class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 使用双指针从两端向中间收缩
        left = 0
        right = len(arr) - 1
        
        # 当剩余元素数量大于k时继续收缩
        while right - left + 1 > k:
            # 比较左右两端元素与x的距离
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        
        # 返回从left到right的子数组
        return arr[left:right+1]
