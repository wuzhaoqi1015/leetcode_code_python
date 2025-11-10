MOD = 10**9 + 7

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 计算1到n中质数的个数
        def count_primes(n):
            if n < 2:
                return 0
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return sum(is_prime)
        
        prime_count = count_primes(n)
        non_prime_count = n - prime_count
        
        # 计算阶乘，同时取模
        def factorial(x):
            res = 1
            for i in range(1, x + 1):
                res = (res * i) % MOD
            return res
        
        # 质数在质数索引上的排列数 * 非质数在非质数索引上的排列数
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD
