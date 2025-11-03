class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # 获取数组中的最大值和最小值
        min_val = min(nums)
        max_val = max(nums)
        
        # 如果所有元素都相等，最大差值为0
        if min_val == max_val:
            return 0
        
        # 计算桶的大小和数量
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # 初始化桶，每个桶存储最小值和最大值
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # 将元素分配到桶中
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        # 计算相邻非空桶之间的最大差值
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            # 跳过空桶
            if buckets[i][0] == float('inf'):
                continue
            # 计算当前桶的最小值与上一个桶的最大值之间的差值
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        return max_gap
