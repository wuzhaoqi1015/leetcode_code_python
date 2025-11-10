class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        # 检查数组本身是否已经严格递增
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        
        # 如果原数组已经严格递增，直接返回True
        if is_strictly_increasing(nums):
            return True
        
        # 遍历每个位置，尝试删除该位置的元素后检查是否严格递增
        for i in range(n):
            # 创建删除第i个元素后的新数组
            new_nums = nums[:i] + nums[i+1:]
            if is_strictly_increasing(new_nums):
                return True
        
        # 如果删除任意一个元素后都不能严格递增，返回False
        return False
