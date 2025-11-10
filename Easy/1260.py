class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        # 计算实际需要移动的次数，避免重复移动
        k = k % total
        if k == 0:
            return grid
        
        # 将二维网格展平为一维列表
        flat_list = []
        for i in range(m):
            for j in range(n):
                flat_list.append(grid[i][j])
        
        # 通过切片操作实现循环右移
        flat_list = flat_list[-k:] + flat_list[:-k]
        
        # 将一维列表重新转换为二维网格
        result = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(flat_list[index])
                index += 1
            result.append(row)
        
        return result
