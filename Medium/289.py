class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        # 定义八个方向
        directions = [(-1,-1), (-1,0), (-1,1),
                     (0,-1),         (0,1),
                     (1,-1),  (1,0),  (1,1)]
        
        # 第一遍遍历：计算每个细胞周围活细胞数量
        for i in range(m):
            for j in range(n):
                # 统计周围活细胞数量
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        # 使用位运算获取原始状态（最低位）
                        if board[ni][nj] & 1:
                            live_neighbors += 1
                
                # 根据规则更新状态，将新状态存储在第二位
                # 规则1和3：活细胞死亡（保持0或变为0）
                # 规则2：活细胞存活（保持1）
                # 规则4：死细胞复活（变为1）
                if board[i][j] & 1:
                    if 2 <= live_neighbors <= 3:
                        board[i][j] |= 2  # 存活，新状态为1
                    # 否则死亡，新状态为0（不需要操作）
                else:
                    if live_neighbors == 3:
                        board[i][j] |= 2  # 复活，新状态为1
        
        # 第二遍遍历：更新为最终状态
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # 右移一位，获取新状态
