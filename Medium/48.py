class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先进行矩阵转置
        for i in range(n):
            for j in range(i + 1, n):
                # 交换matrix[i][j]和matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 再对每一行进行反转
        for i in range(n):
            # 反转第i行
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
