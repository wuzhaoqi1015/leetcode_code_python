MOD = 10**9 + 7

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = [0] * 101  # 因为arr[i]范围是0-100
        for num in arr:
            count[num] += 1
        
        res = 0
        
        # 遍历所有可能的x, y, z组合
        for x in range(101):
            if count[x] == 0:
                continue
            for y in range(x, 101):  # 从x开始避免重复
                if count[y] == 0:
                    continue
                z = target - x - y
                if z < y or z > 100:  # 保持x<=y<=z的顺序
                    continue
                if count[z] == 0:
                    continue
                
                # 计算组合数
                if x == y == z:
                    # C(n,3) = n*(n-1)*(n-2)//6
                    n = count[x]
                    res = (res + n * (n-1) * (n-2) // 6) % MOD
                elif x == y:
                    # C(n,2) * count[z]
                    n = count[x]
                    res = (res + n * (n-1) // 2 * count[z]) % MOD
                elif y == z:
                    # count[x] * C(n,2)
                    n = count[y]
                    res = (res + count[x] * n * (n-1) // 2) % MOD
                else:
                    # count[x] * count[y] * count[z]
                    res = (res + count[x] * count[y] * count[z]) % MOD
        
        return res
