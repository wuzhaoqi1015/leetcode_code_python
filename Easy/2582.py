class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 计算一个完整周期的长度
        cycle_length = 2 * (n - 1)
        # 计算在周期内的相对时间
        relative_time = time % cycle_length
        # 如果相对时间小于n-1，说明在正向传递过程中
        if relative_time < n:
            return relative_time + 1
        else:
            # 否则在反向传递过程中
            return 2 * n - relative_time - 1
