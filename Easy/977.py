class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # 初始化结果数组
        left, right = 0, n - 1  # 双指针分别指向数组首尾
        pos = n - 1  # 从结果数组的末尾开始填充
        
        # 使用双指针从两端向中间遍历
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            
            # 比较两端的平方值，将较大的放入结果数组末尾
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
        
        return result
