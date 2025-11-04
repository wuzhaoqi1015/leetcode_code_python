class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 使用双指针方法，左指针从数组开头开始，右指针从数组末尾开始
        left = 0
        right = len(numbers) - 1
        
        # 当左指针小于右指针时循环
        while left < right:
            # 计算当前两个指针指向的元素之和
            current_sum = numbers[left] + numbers[right]
            
            # 如果和等于目标值，返回下标（注意题目要求下标从1开始）
            if current_sum == target:
                return [left + 1, right + 1]
            # 如果和小于目标值，左指针右移以增大和
            elif current_sum < target:
                left += 1
            # 如果和大于目标值，右指针左移以减小和
            else:
                right -= 1
        
        # 根据题目保证有解，这里不会执行到
        return [-1, -1]
