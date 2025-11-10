class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # 初始化行和列的计数数组
        row_count = [0] * m
        col_count = [0] * n
        
        # 统计每行和每列被操作的次数
        for ri, ci in indices:
            row_count[ri] += 1
            col_count[ci] += 1
        
        # 计算奇数单元格的数量
        odd_count = 0
        for i in range(m):
            for j in range(n):
                # 单元格(i,j)的值等于行i的操作次数加上列j的操作次数
                if (row_count[i] + col_count[j]) % 2 == 1:
                    odd_count += 1
        
        return odd_count
