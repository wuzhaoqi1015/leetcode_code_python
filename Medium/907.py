class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n  # 存储每个元素左边第一个比它小的元素位置
        right = [0] * n  # 存储每个元素右边第一个比它小的元素位置
        
        # 单调栈计算left数组
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # 单调栈计算right数组
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # 计算总和
        result = 0
        for i in range(n):
            # 计算以arr[i]为最小值的子数组个数
            count = (i - left[i]) * (right[i] - i)
            result = (result + arr[i] * count) % MOD
            
        return result
