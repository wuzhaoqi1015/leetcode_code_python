class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # 从边界开始DFS标记所有与边界相连的'O'为临时标记'T'
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # 临时标记
            # 四个方向DFS
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # 遍历四条边界
        for i in range(m):
            dfs(i, 0)        # 左边界
            dfs(i, n - 1)    # 右边界
        
        for j in range(n):
            dfs(0, j)        # 上边界
            dfs(m - 1, j)    # 下边界
        
        # 遍历整个矩阵，将剩余的'O'改为'X'，将'T'恢复为'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
