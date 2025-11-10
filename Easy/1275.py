class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 初始化3x3棋盘
        board = [[' ' for _ in range(3)] for _ in range(3)]
        
        # 填充棋盘
        for i, move in enumerate(moves):
            row, col = move
            if i % 2 == 0:
                board[row][col] = 'X'  # A玩家
            else:
                board[row][col] = 'O'  # B玩家
        
        # 检查所有可能的获胜情况
        for i in range(3):
            # 检查行
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return 'A' if board[i][0] == 'X' else 'B'
            # 检查列
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return 'A' if board[0][i] == 'X' else 'B'
        
        # 检查对角线
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return 'A' if board[0][0] == 'X' else 'B'
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return 'A' if board[0][2] == 'X' else 'B'
        
        # 检查游戏是否结束
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
