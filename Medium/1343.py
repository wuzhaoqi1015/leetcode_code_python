class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # 计算目标子数组和的最小值
        target_sum = k * threshold
        # 初始化当前窗口和
        current_sum = 0
        # 初始化符合条件的子数组个数
        count = 0
        
        # 计算初始窗口的和
        for i in range(k):
            current_sum += arr[i]
        
        # 检查初始窗口是否满足条件
        if current_sum >= target_sum:
            count += 1
        
        # 滑动窗口遍历数组
        for i in range(k, len(arr)):
            # 更新窗口和：减去离开窗口的元素，加上新进入窗口的元素
            current_sum = current_sum - arr[i - k] + arr[i]
            # 检查当前窗口和是否满足条件
            if current_sum >= target_sum:
                count += 1
        
        return count
