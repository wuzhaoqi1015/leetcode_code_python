class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 首先找到白车R的位置
        rook_row, rook_col = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
        
        count = 0
        # 定义四个方向：上、右、下、左
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dx, dy in directions:
            x, y = rook_row, rook_col
            # 沿着每个方向移动直到遇到边界或棋子
            while True:
                x += dx
                y += dy
                # 检查是否超出棋盘边界
                if x < 0 or x >= 8 or y < 0 or y >= 8:
                    break
                # 如果遇到白象B，则停止该方向的搜索
                if board[x][y] == 'B':
                    break
                # 如果遇到黑卒p，则计数并停止该方向的搜索
                if board[x][y] == 'p':
                    count += 1
                    break
        
        return count
