class Solution:
    def countPrimes(self, n: int) -> int:
        # 处理边界情况：n小于等于2时没有质数
        if n <= 2:
            return 0
        
        # 初始化标记数组，长度为n，初始都标记为质数（True）
        is_prime = [True] * n
        # 0和1不是质数
        is_prime[0] = is_prime[1] = False
        
        # 使用埃拉托斯特尼筛法
        # 只需要遍历到sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # 将i的所有倍数标记为非质数
                # 从i*i开始标记，因为更小的倍数已经被之前的质数标记过了
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # 统计所有标记为质数的数量
        return sum(is_prime)
