class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # 对数组进行排序以便后续处理
        nums.sort()
        n = len(nums)
        
        # 遍历所有可能的x值（从0到n）
        for x in range(n + 1):
            # 计算大于等于x的元素个数
            # 使用二分查找找到第一个大于等于x的位置
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            
            # 大于等于x的元素个数为n - left
            count = n - left
            
            # 检查是否满足特殊数组条件
            if count == x:
                return x
        
        # 如果没有找到符合条件的x，返回-1
        return -1
