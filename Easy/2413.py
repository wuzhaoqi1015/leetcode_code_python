class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # 如果n是偶数，最小公倍数就是n本身
        # 如果n是奇数，最小公倍数就是2*n
        if n % 2 == 0:
            return n
        else:
            return 2 * n
