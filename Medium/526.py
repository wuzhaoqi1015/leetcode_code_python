class Solution:
    def countArrangement(self, n: int) -> int:
        # 使用回溯法解决优美排列问题
        self.count = 0  # 计数器，记录优美排列的数量
        used = [False] * (n + 1)  # 标记数组，记录数字是否已被使用
        
        def backtrack(pos):
            # 如果已经处理完所有位置，找到一个有效排列
            if pos > n:
                self.count += 1
                return
            
            # 尝试将每个未使用的数字放在当前位置
            for num in range(1, n + 1):
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True  # 标记该数字已使用
                    backtrack(pos + 1)  # 递归处理下一个位置
                    used[num] = False  # 回溯，撤销选择
        
        backtrack(1)  # 从位置1开始回溯
        return self.count
