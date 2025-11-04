class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 初始化丑数列表，第一个丑数为1
        ugly = [1]
        # 三个指针分别对应2、3、5的倍数
        i2, i3, i5 = 0, 0, 0
        
        # 生成第n个丑数
        for _ in range(1, n):
            # 计算三个指针指向的丑数乘以对应因子的值
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5
            
            # 取最小值作为下一个丑数
            next_ugly = min(next2, next3, next5)
            ugly.append(next_ugly)
            
            # 更新指针，如果当前丑数等于某个指针计算的结果，则该指针加1
            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1
        
        # 返回第n个丑数
        return ugly[-1]
