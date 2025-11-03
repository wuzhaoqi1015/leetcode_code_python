class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # 首先对数组进行排序
        n = len(nums)
        closest_sum = float('inf')  # 初始化最接近的和为无穷大
        
        for i in range(n - 2):  # 固定第一个数，遍历到倒数第三个数
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
                continue
                
            left = i + 1  # 左指针指向当前数的下一个
            right = n - 1  # 右指针指向数组末尾
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # 计算当前三数之和
                
                if current_sum == target:  # 如果正好等于目标值，直接返回
                    return current_sum
                
                # 更新最接近的和
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:  # 如果当前和小于目标值，左指针右移
                    left += 1
                else:  # 如果当前和大于目标值，右指针左移
                    right -= 1
        
        return closest_sum
