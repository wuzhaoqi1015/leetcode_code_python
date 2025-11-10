class Solution:
    def distinctIntegers(self, n: int) -> int:
        # 初始时桌面上只有n
        # 观察规律：每天会添加满足 x % i == 1 的i
        # 实际上这个过程会不断添加n-1, n-2, ..., 2
        # 因为对于任何k (2<=k<=n-1)，总存在x=k+1使得x%k==1
        # 最终桌面上会有从2到n的所有数字
        # 特殊情况：当n=1时，没有其他数字能满足条件，只有1本身
        if n == 1:
            return 1
        else:
            # 从2到n的所有数字都会出现在桌面上
            return n - 1
