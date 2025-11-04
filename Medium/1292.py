class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 构建二维前缀和数组
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
        
        # 二分查找最大边长
        def check(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    # 计算边长为k的正方形区域和
                    total = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
                    if total <= threshold:
                        return True
            return False
        
        left, right = 0, min(m, n)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
