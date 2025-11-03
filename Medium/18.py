class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()  # 排序便于去重和双指针操作
        res = []
        
        for i in range(n - 3):
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 提前终止条件
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # 跳过重复的第二个数
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # 提前终止条件
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                    
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # 跳过重复的第三个数
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 跳过重复的第四个数
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
