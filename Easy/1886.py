class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 检查原始矩阵是否匹配
        if mat == target:
            return True
        
        n = len(mat)
        # 旋转90度
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n-1-i] = mat[i][j]
        if rotated == target:
            return True
        
        # 旋转180度
        rotated2 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated2[n-1-i][n-1-j] = mat[i][j]
        if rotated2 == target:
            return True
        
        # 旋转270度
        rotated3 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated3[n-1-j][i] = mat[i][j]
        if rotated3 == target:
            return True
        
        return False
