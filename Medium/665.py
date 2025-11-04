class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0  # 记录需要修改的次数
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:  # 发现逆序对
                count += 1
                if count > 1:  # 如果修改次数超过1次，直接返回False
                    return False
                
                # 当出现逆序时，有两种修改策略：
                # 1. 将nums[i]降低为nums[i+1]
                # 2. 将nums[i+1]升高为nums[i]
                # 我们需要选择对后续影响较小的修改方式
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    # 如果nums[i+1]比nums[i-1]还小，那么只能选择升高nums[i+1]
                    nums[i + 1] = nums[i]
                else:
                    # 否则选择降低nums[i]对后续影响更小
                    nums[i] = nums[i + 1]
        
        return True
