class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0  # 初始化串联值
        left, right = 0, len(nums) - 1  # 使用双指针指向数组的首尾
        
        while left <= right:
            if left == right:  # 如果只剩一个元素
                total += nums[left]
                break
            else:  # 如果还有多个元素
                # 将首尾元素转换为字符串后拼接，再转换为整数
                concat_val = int(str(nums[left]) + str(nums[right]))
                total += concat_val
                left += 1  # 移动左指针
                right -= 1  # 移动右指针
        
        return total  # 返回最终的串联值
