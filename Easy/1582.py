class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # 预处理每行和每列的1的个数
        row_count = [0] * m
        col_count = [0] * n
        
        # 统计每行和每列的1的个数
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        result = 0
        # 遍历矩阵，检查每个位置是否为特殊位置
        for i in range(m):
            for j in range(n):
                # 当前位置为1，且所在行和列都只有这1个1
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    result += 1
        
        return result
