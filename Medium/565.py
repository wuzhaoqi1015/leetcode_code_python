class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n  # 标记数组，记录是否访问过
        max_length = 0  # 记录最大环长度
        
        for i in range(n):
            if not visited[i]:
                count = 0
                current = i
                # 遍历当前环
                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    count += 1
                # 更新最大环长度
                if count > max_length:
                    max_length = count
        
        return max_length
