class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化n x n矩阵，所有元素为0
        matrix = [[0] * n for _ in range(n)]
        
        # 定义四个方向：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # 初始化当前位置和方向索引
        row, col = 0, 0
        direction_index = 0
        
        # 填充数字从1到n*n
        for num in range(1, n * n + 1):
            matrix[row][col] = num
            
            # 计算下一个位置
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
            
            # 检查下一个位置是否越界或已被填充
            if (next_row < 0 or next_row >= n or 
                next_col < 0 or next_col >= n or 
                matrix[next_row][next_col] != 0):
                # 改变方向
                direction_index = (direction_index + 1) % 4
                next_row = row + directions[direction_index][0]
                next_col = col + directions[direction_index][1]
            
            row, col = next_row, next_col
        
        return matrix
