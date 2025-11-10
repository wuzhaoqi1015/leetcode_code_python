class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 将三种水的需求量排序
        a, b, c = sorted(amount)
        
        # 如果最大的需求量大于等于其他两个需求量的和
        # 那么总时间就是最大需求量
        if c >= a + b:
            return c
        
        # 否则，总时间等于所有需求量的总和向上取整除以2
        # 因为每次最多可以装两杯
        return (a + b + c + 1) // 2
