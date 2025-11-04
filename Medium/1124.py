class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 将工作时间转换为劳累标记：劳累为1，不劳累为-1
        n = len(hours)
        score = [1 if h > 8 else -1 for h in hours]
        
        # 计算前缀和
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + score[i - 1]
        
        # 使用单调栈记录前缀和的递减序列
        stack = []
        for i in range(len(prefix_sum)):
            if not stack or prefix_sum[stack[-1]] > prefix_sum[i]:
                stack.append(i)
        
        # 从后往前遍历寻找最大长度
        max_len = 0
        j = len(prefix_sum) - 1
        while j >= 0:
            while stack and prefix_sum[stack[-1]] < prefix_sum[j]:
                max_len = max(max_len, j - stack[-1])
                stack.pop()
            j -= 1
        
        return max_len
