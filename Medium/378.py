class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        
        # 二分查找
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = n - 1
            
            # 统计小于等于mid的元素个数
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            
            # 调整搜索范围
            if count < k:
                left = mid + 1
            else:
                right = mid
                
        return left
