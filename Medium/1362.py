class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        import math
        
        def find_closest_factors(n):
            # 从平方根开始向下寻找最近的因数对
            start = int(math.isqrt(n))
            for i in range(start, 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return [1, n]  # 理论上不会执行到这里
        
        # 计算num+1和num+2的最接近因数对
        cand1 = find_closest_factors(num + 1)
        cand2 = find_closest_factors(num + 2)
        
        # 比较两个候选对的绝对差，选择差值较小的
        if abs(cand1[0] - cand1[1]) < abs(cand2[0] - cand2[1]):
            return cand1
        else:
            return cand2
