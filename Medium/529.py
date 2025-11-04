class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 定义八个方向的偏移量
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        rows, cols = len(board), len(board[0])
        
        def count_mines(r, c):
            # 计算当前位置周围的地雷数量
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def dfs(r, c):
            # 如果当前位置超出边界或不是未挖出的方块，直接返回
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'E':
                return
            
            # 计算周围地雷数量
            mine_count = count_mines(r, c)
            
            if mine_count > 0:
                # 如果有相邻地雷，显示数字
                board[r][c] = str(mine_count)
            else:
                # 如果没有相邻地雷，标记为'B'并递归揭露相邻方块
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
        
        click_r, click_c = click
        # 如果点击到地雷，游戏结束
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            # 否则进行深度优先搜索揭露方块
            dfs(click_r, click_c)
        
        return board
