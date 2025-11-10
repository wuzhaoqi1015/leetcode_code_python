class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        # 遍历每一行
        for i in range(n):
            # 主对角线元素
            total += mat[i][i]
            # 副对角线元素，当矩阵大小为奇数且处于中心点时跳过重复计算
            if i != n - 1 - i:
                total += mat[i][n - 1 - i]
        return total
