class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 初始化最小值和最大值，分别记录当前遍历到的最小值和最大值
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        
        # 从第二个数组开始遍历
        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            # 计算当前数组的最小值与之前最大值的距离
            # 计算当前数组的最大值与之前最小值的距离
            # 取两者中的较大值更新结果
            result = max(result, abs(curr_max - min_val), abs(max_val - curr_min))
            
            # 更新全局最小值和最大值
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return result
