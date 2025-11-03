class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数和列数
        m = len(matrix)
        n = len(matrix[0])
        
        # 使用二分查找定位目标值
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # 将一维索引转换为二维坐标
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
