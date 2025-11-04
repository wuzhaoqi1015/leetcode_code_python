class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 使用滑动窗口方法
        n = len(nums)
        left = 0  # 窗口左边界
        current_sum = 0  # 当前窗口和
        min_length = float('inf')  # 最小长度，初始设为无穷大
        
        # 遍历数组，移动窗口右边界
        for right in range(n):
            current_sum += nums[right]  # 扩展窗口
            
            # 当窗口和满足条件时，尝试收缩窗口
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 收缩窗口左边界
                current_sum -= nums[left]
                left += 1
        
        # 如果找到了符合条件的子数组，返回最小长度，否则返回0
        return min_length if min_length != float('inf') else 0
