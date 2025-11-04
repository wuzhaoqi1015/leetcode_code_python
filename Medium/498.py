class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        # 方向标志：1表示向上遍历，-1表示向下遍历
        direction = 1
        
        for i in range(m * n):
            result.append(mat[row][col])
            
            # 根据当前方向计算下一个位置
            if direction == 1:  # 向上遍历
                if col == n - 1:  # 到达右边界
                    row += 1
                    direction = -1
                elif row == 0:  # 到达上边界
                    col += 1
                    direction = -1
                else:  # 正常向上移动
                    row -= 1
                    col += 1
            else:  # 向下遍历
                if row == m - 1:  # 到达下边界
                    col += 1
                    direction = 1
                elif col == 0:  # 到达左边界
                    row += 1
                    direction = 1
                else:  # 正常向下移动
                    row += 1
                    col -= 1
        
        return result
