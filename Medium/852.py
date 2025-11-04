class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            # 如果中间元素大于右侧元素，说明峰值在左侧或中间
            if arr[mid] > arr[mid + 1]:
                right = mid
            # 否则峰值在右侧
            else:
                left = mid + 1
        # 当left==right时，即为峰值位置
        return left
