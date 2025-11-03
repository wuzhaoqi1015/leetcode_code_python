class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 初始化行、列、九宫格的集合
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 遍历数独的每个单元格
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                # 跳过空白格
                if num == '.':
                    continue
                
                # 检查当前数字是否在行、列或九宫格中已存在
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                # 计算当前单元格所属的九宫格索引
                box_index = (i // 3) * 3 + j // 3
                if num in boxes[box_index]:
                    return False
                
                # 将当前数字添加到对应的行、列和九宫格集合中
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        # 所有检查通过，返回True
        return True
