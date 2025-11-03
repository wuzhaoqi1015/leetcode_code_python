class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # 检查第一行是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
                
        # 检查第一列是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        # 使用第一行和第一列作为标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 根据标记设置矩阵内部元素为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 处理第一行
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # 处理第一列
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
