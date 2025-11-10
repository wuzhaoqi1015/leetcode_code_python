class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 对数组进行排序，以便选择最小的元素来形成最长的子序列
        nums.sort()
        n = len(nums)
        m = len(queries)
        
        # 计算前缀和数组
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # 初始化结果数组
        answer = [0] * m
        
        # 对于每个查询，使用二分查找找到最大的前缀和不超过查询值的位置
        for i in range(m):
            left, right = 0, n
            while left < right:
                mid = (left + right + 1) // 2
                if prefix_sum[mid] <= queries[i]:
                    left = mid
                else:
                    right = mid - 1
            answer[i] = left
        
        return answer
