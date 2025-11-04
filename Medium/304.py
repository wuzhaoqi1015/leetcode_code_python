class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return
        
        m, n = len(matrix), len(matrix[0])
        # 创建前缀和矩阵，大小比原矩阵多一行一列，方便边界处理
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 计算前缀和矩阵
        for i in range(m):
            for j in range(n):
                # 前缀和公式：当前值 + 上方前缀和 + 左方前缀和 - 左上方前缀和
                self.prefix[i+1][j+1] = matrix[i][j] + self.prefix[i][j+1] + self.prefix[i+1][j] - self.prefix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 使用前缀和矩阵计算区域和
        # 公式：右下角前缀和 - 上方前缀和 - 左方前缀和 + 左上方前缀和
        return (self.prefix[row2+1][col2+1] 
                - self.prefix[row1][col2+1] 
                - self.prefix[row2+1][col1] 
                + self.prefix[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
