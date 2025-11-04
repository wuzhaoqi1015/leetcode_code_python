class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # 统计每行和每列的服务器数量
        row_count = [0] * m
        col_count = [0] * n
        
        # 第一次遍历：统计每行和每列的服务器总数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        result = 0
        # 第二次遍历：检查每个服务器是否能与其他服务器通信
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 如果该行或该列有至少2台服务器，则该服务器可以通信
                    if row_count[i] > 1 or col_count[j] > 1:
                        result += 1
        
        return result
