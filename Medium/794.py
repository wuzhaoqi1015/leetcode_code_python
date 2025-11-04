class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # 统计X和O的数量
        x_count = 0
        o_count = 0
        for row in board:
            for cell in row:
                if cell == 'X':
                    x_count += 1
                elif cell == 'O':
                    o_count += 1
        
        # 检查数量关系：X的数量必须等于O的数量或比O多1
        if not (x_count == o_count or x_count == o_count + 1):
            return False
        
        # 检查是否有玩家获胜
        x_win = False
        o_win = False
        
        # 检查行
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                if board[i][0] == 'X':
                    x_win = True
                else:
                    o_win = True
        
        # 检查列
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != ' ':
                if board[0][j] == 'X':
                    x_win = True
                else:
                    o_win = True
        
        # 检查对角线
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            if board[0][0] == 'X':
                x_win = True
            else:
                o_win = True
        
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            if board[0][2] == 'X':
                x_win = True
            else:
                o_win = True
        
        # 如果两个玩家都获胜，不合法
        if x_win and o_win:
            return False
        
        # 如果X获胜，X的数量必须比O多1
        if x_win and x_count != o_count + 1:
            return False
        
        # 如果O获胜，X和O的数量必须相等
        if o_win and x_count != o_count:
            return False
        
        return True
