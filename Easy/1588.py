class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        
        # 计算前缀和数组
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        # 遍历所有可能的奇数长度子数组
        for length in range(1, n + 1, 2):  # 步长为2，只考虑奇数长度
            for start in range(n - length + 1):
                end = start + length - 1
                # 使用前缀和计算子数组和
                total_sum += prefix_sum[end + 1] - prefix_sum[start]
        
        return total_sum
