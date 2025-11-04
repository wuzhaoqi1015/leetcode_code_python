class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = []
        num = n
        while num != 0:
            remainder = num % (-2)
            num = num // (-2)
            if remainder < 0:
                remainder += 2
                num += 1
            res.append(str(remainder))
        return ''.join(res[::-1])
