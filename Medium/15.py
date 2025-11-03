class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先对数组进行排序
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # 跳过重复的起始元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 如果当前元素已经大于0，由于数组已排序，后面的元素都大于0，不可能和为0
            if nums[i] > 0:
                break
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的left元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的right元素  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # 和太小，需要增大
                else:
                    right -= 1  # 和太大，需要减小
                    
        return result
