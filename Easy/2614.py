class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        # 判断是否为质数的辅助函数
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        
        n = len(nums)
        max_prime = 0
        
        # 遍历两条对角线
        for i in range(n):
            # 主对角线元素
            val1 = nums[i][i]
            if val1 > max_prime and is_prime(val1):
                max_prime = val1
            
            # 副对角线元素
            val2 = nums[i][n - i - 1]
            if val2 > max_prime and is_prime(val2):
                max_prime = val2
        
        return max_prime
