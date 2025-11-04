class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # 将绝对值表达式拆分为四种情况，分别计算最大值与最小值的差
        n = len(arr1)
        # 初始化四种情况的列表
        case1 = [arr1[i] + arr2[i] + i for i in range(n)]
        case2 = [arr1[i] + arr2[i] - i for i in range(n)]
        case3 = [arr1[i] - arr2[i] + i for i in range(n)]
        case4 = [arr1[i] - arr2[i] - i for i in range(n)]
        
        # 计算每种情况的最大值和最小值
        max1, min1 = max(case1), min(case1)
        max2, min2 = max(case2), min(case2)
        max3, min3 = max(case3), min(case3)
        max4, min4 = max(case4), min(case4)
        
        # 返回四种情况中的最大值
        return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
