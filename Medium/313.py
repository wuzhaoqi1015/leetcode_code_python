class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 初始化丑数列表，第一个丑数为1
        ugly = [1]
        # 创建指针列表，每个质数对应一个指针，初始都指向第一个丑数
        pointers = [0] * len(primes)
        
        # 生成第n个超级丑数
        while len(ugly) < n:
            # 计算每个质数与对应指针指向的丑数的乘积
            next_uglies = [primes[i] * ugly[pointers[i]] for i in range(len(primes))]
            # 找出最小的乘积作为下一个丑数
            next_ugly = min(next_uglies)
            ugly.append(next_ugly)
            
            # 更新指针：所有产生最小乘积的指针都向前移动一位
            for i in range(len(primes)):
                if primes[i] * ugly[pointers[i]] == next_ugly:
                    pointers[i] += 1
        
        # 返回第n个超级丑数
        return ugly[n-1]
