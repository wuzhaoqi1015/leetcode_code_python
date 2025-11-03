class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 定义深度优先搜索函数
        def dfs(i, j, k):
            # 如果索引越界或当前字符不匹配，返回False
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 如果已经匹配到单词最后一个字符，返回True
            if k == len(word) - 1:
                return True
            # 临时存储当前字符，并将当前位置标记为已访问
            tmp, board[i][j] = board[i][j], '/'
            # 向四个方向进行深度优先搜索
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 恢复当前位置的原始字符
            board[i][j] = tmp
            return res

        # 遍历网格中的每个单元格
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 从每个单元格开始尝试匹配单词
                if dfs(i, j, 0):
                    return True
        return False
