class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # 当n=1时，概率为1；当n>1时，概率为0.5
        if n == 1:
            return 1.0
        else:
            return 0.5
