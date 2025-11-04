class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 使用归并排序实现O(nlogn)时间复杂度和O(n)空间复杂度
        if len(nums) <= 1:
            return nums
        
        # 分割数组
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # 合并两个有序数组
        return self.merge(left, right)
    
    def merge(self, left, right):
        merged = []
        i = j = 0
        
        # 比较两个数组的元素，按顺序合并
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # 添加剩余元素
        while i < len(left):
            merged.append(left[i])
            i += 1
            
        while j < len(right):
            merged.append(right[j])
            j += 1
            
        return merged
