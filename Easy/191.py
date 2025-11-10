class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # 使用位运算，每次消除最低位的1
        while n:
            n &= n - 1  # 这个操作会将最低位的1变为0
            count += 1
        return count
