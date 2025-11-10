class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # 生成所有单元格坐标
        cells = [[i, j] for i in range(rows) for j in range(cols)]
        # 按曼哈顿距离排序
        cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
        return cells
