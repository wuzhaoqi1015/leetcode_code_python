class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # 优先取1，然后取0，最后取-1
        if k <= numOnes:
            # 如果k不超过1的数量，全取1
            return k
        elif k <= numOnes + numZeros:
            # 如果k不超过1和0的总数，取完所有1后取0
            return numOnes
        else:
            # 需要取部分-1，计算需要取多少个-1
            neg_used = k - numOnes - numZeros
            return numOnes - neg_used
