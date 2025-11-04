class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # dp0表示以arr[i]结尾且没有删除元素的最大子数组和
        # dp1表示以arr[i]结尾且删除了一个元素的最大子数组和
        dp0 = [0] * n
        dp1 = [0] * n
        
        dp0[0] = arr[0]
        dp1[0] = -10**9  # 第一个元素无法删除，初始化为极小值
        
        res = arr[0]
        
        for i in range(1, n):
            # 没有删除的情况：要么延续前面的子数组，要么从当前元素重新开始
            dp0[i] = max(dp0[i-1] + arr[i], arr[i])
            
            # 删除一个元素的情况：
            # 1. 删除当前元素，那么就是dp0[i-1]（前面没删除的最大和）
            # 2. 之前已经删除过元素，现在延续dp1[i-1] + arr[i]
            dp1[i] = max(dp0[i-1], dp1[i-1] + arr[i])
            
            # 更新结果，考虑两种情况的最大值
            res = max(res, dp0[i], dp1[i])
        
        return res
