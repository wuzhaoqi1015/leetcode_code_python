class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 先对数组进行排序
        nums.sort()
        n = len(nums)
        count = 0
        
        # 固定最大的边作为第三条边
        for k in range(n-1, 1, -1):
            i = 0
            j = k - 1
            # 使用双指针寻找满足条件的两条边
            while i < j:
                # 如果两边之和大于第三边，则所有i到j-1的边都满足条件
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
                    
        return count
