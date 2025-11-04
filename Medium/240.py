class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # 从矩阵右上角开始搜索
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            # 如果当前元素大于目标值，向左移动一列
            elif matrix[row][col] > target:
                col -= 1
            # 如果当前元素小于目标值，向下移动一行
            else:
                row += 1
        return False
