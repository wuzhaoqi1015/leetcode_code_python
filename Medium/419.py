class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 初始化舰队数量
        count = 0
        # 获取棋盘的行数和列数
        m, n = len(board), len(board[0])
        
        # 遍历棋盘的每一个单元格
        for i in range(m):
            for j in range(n):
                # 如果当前单元格不是战舰，跳过
                if board[i][j] != 'X':
                    continue
                
                # 检查当前战舰是否是舰队的头部
                # 水平方向：如果左边有战舰，说明当前不是头部
                if i > 0 and board[i-1][j] == 'X':
                    continue
                # 垂直方向：如果上边有战舰，说明当前不是头部
                if j > 0 and board[i][j-1] == 'X':
                    continue
                
                # 当前战舰是舰队头部，计数加1
                count += 1
        
        return count
