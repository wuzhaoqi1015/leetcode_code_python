class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        # 从左边开始找到第一个下降的位置
        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        # 检查峰值位置是否在数组中间（不能是第一个或最后一个元素）
        if i == 0 or i == n - 1:
            return False
        
        # 从峰值位置开始检查是否严格递减
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        # 如果遍历到了最后一个元素，说明是有效的山脉数组
        return i == n - 1
