class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # 将皇后的位置转换为集合以便快速查找
        queen_set = set((x, y) for x, y in queens)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # 左上、上、右上
            (0, -1),           (0, 1),   # 左、右
            (1, -1),  (1, 0),  (1, 1)    # 左下、下、右下
        ]
        result = []
        kx, ky = king
        
        # 检查每个方向
        for dx, dy in directions:
            x, y = kx, ky
            # 沿着当前方向移动直到超出棋盘边界
            while True:
                x += dx
                y += dy
                # 检查是否超出棋盘边界
                if x < 0 or x >= 8 or y < 0 or y >= 8:
                    break
                # 如果当前位置有皇后，则加入结果并停止该方向的搜索
                if (x, y) in queen_set:
                    result.append([x, y])
                    break
        
        return result
