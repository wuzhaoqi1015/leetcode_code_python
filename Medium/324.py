class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 复制并排序数组
        sorted_nums = sorted(nums)
        
        n = len(nums)
        # 计算中间位置，用于分割较小和较大的数
        mid = (n + 1) // 2
        
        # 使用双指针从中间和末尾开始填充
        # 较小部分从mid-1开始向左，较大部分从n-1开始向左
        left = mid - 1
        right = n - 1
        
        # 交替填充较小和较大的数到原数组
        for i in range(n):
            if i % 2 == 0:
                # 偶数位置放较小的数
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                # 奇数位置放较大的数
                nums[i] = sorted_nums[right]
                right -= 1
