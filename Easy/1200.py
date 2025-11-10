class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 首先对数组进行排序，便于计算相邻元素的差值
        arr.sort()
        min_diff = float('inf')
        result = []
        
        # 遍历排序后的数组，计算相邻元素的差值
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            # 如果找到更小的差值，更新最小差值并清空结果列表
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i-1], arr[i]]]
            # 如果差值等于当前最小差值，将元素对添加到结果列表
            elif diff == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result
