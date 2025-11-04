class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # 首先对数组进行排序
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)  # 前缀和数组，prefix[i]表示前i个元素的和
        
        # 计算前缀和
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        # 二分查找可能的value值范围
        left, right = 0, max(arr)
        best_value = 0
        min_diff = float('inf')
        
        # 二分查找
        while left <= right:
            mid = (left + right) // 2
            # 找到第一个大于等于mid的索引
            idx = bisect.bisect_left(arr, mid)
            # 计算当前value下的数组和
            current_sum = prefix[idx] + (n - idx) * mid
            
            # 计算与target的差值
            diff = abs(current_sum - target)
            
            # 如果找到更小的差值，或者差值相同但value更小，则更新结果
            if diff < min_diff or (diff == min_diff and mid < best_value):
                min_diff = diff
                best_value = mid
            
            # 根据当前和与target的关系调整搜索范围
            if current_sum < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return best_value

# 需要导入bisect模块
import bisect
