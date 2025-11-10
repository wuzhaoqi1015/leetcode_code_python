class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # 对数组进行排序，便于每次取最小值和最大值
        nums.sort()
        # 使用集合来存储不同的平均值，避免重复
        avg_set = set()
        # 使用双指针，左指针指向当前最小值，右指针指向当前最大值
        left, right = 0, len(nums) - 1
        # 当左指针小于右指针时循环
        while left < right:
            # 计算当前最小值和最大值的平均值
            current_avg = (nums[left] + nums[right]) / 2
            # 将平均值添加到集合中
            avg_set.add(current_avg)
            # 移动指针，相当于删除最小值和最大值
            left += 1
            right -= 1
        # 返回集合中不同平均值的数量
        return len(avg_set)
