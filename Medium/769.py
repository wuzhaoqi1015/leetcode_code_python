class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 初始化最大值和块数计数器
        max_val = -1
        count = 0
        
        # 遍历数组中的每个元素及其索引
        for i, num in enumerate(arr):
            # 更新当前遇到的最大值
            max_val = max(max_val, num)
            # 如果当前索引等于最大值，说明可以形成一个块
            if i == max_val:
                count += 1
                
        return count
