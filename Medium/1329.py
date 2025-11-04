class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # 处理所有对角线，从第一行和第一列开始
        # 从第一列开始的对角线（除了(0,0)）
        for i in range(1, m):
            diag = []
            row, col = i, 0
            # 收集对角线元素
            while row < m and col < n:
                diag.append(mat[row][col])
                row += 1
                col += 1
            # 排序
            diag.sort()
            # 放回排序后的元素
            row, col = i, 0
            idx = 0
            while row < m and col < n:
                mat[row][col] = diag[idx]
                row += 1
                col += 1
                idx += 1
        
        # 从第一行开始的对角线
        for j in range(n):
            diag = []
            row, col = 0, j
            # 收集对角线元素
            while row < m and col < n:
                diag.append(mat[row][col])
                row += 1
                col += 1
            # 排序
            diag.sort()
            # 放回排序后的元素
            row, col = 0, j
            idx = 0
            while row < m and col < n:
                mat[row][col] = diag[idx]
                row += 1
                col += 1
                idx += 1
        
        return mat
