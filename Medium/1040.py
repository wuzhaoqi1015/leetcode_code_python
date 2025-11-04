class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        # 计算最大移动次数
        # 最大移动次数等于总空位数减去较小的端点空位
        max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
        
        # 计算最小移动次数
        min_moves = n
        j = 0
        for i in range(n):
            # 找到满足窗口大小小于n的最大j
            while j < n - 1 and stones[j + 1] - stones[i] < n:
                j += 1
            # 计算当前窗口内的石子数
            stones_in_window = j - i + 1
            # 特殊情况：如果窗口内有n-1个石子且空位正好是1，需要2次移动
            if stones_in_window == n - 1 and stones[j] - stones[i] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - stones_in_window)
        
        return [min_moves, max_moves]
