class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors_sum(n):
            divisors = set()
            # 遍历到sqrt(n)即可找到所有因数
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    # 如果因数超过4个，提前返回0
                    if len(divisors) > 4:
                        return 0
            # 检查是否恰好有4个因数
            if len(divisors) == 4:
                return sum(divisors)
            return 0
        
        total = 0
        for num in nums:
            total += get_divisors_sum(num)
        return total
