class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 使用双指针法，从数组两端向中间移动
        left = 0  # 左指针
        right = len(height) - 1  # 右指针
        max_area = 0  # 记录最大面积
        
        # 当左右指针未相遇时继续循环
        while left < right:
            # 计算当前容器的面积
            current_area = min(height[left], height[right]) * (right - left)
            # 更新最大面积
            max_area = max(max_area, current_area)
            
            # 移动高度较小的指针，因为移动高度较大的指针不会得到更大的面积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
