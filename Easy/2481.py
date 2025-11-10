class Solution:
    def numberOfCuts(self, n: int) -> int:
        # 如果n为1，不需要切割，因为整个圆就是1等分
        if n == 1:
            return 0
        # 如果n是偶数，可以通过直径切割，每次切割同时产生两个等分
        # 因此切割次数为n/2
        elif n % 2 == 0:
            return n // 2
        # 如果n是奇数，每次切割只能增加一个等分
        # 因此需要n次切割
        else:
            return n
