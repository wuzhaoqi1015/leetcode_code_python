class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # 初始化结果列表，包含起始点
        result = [[rStart, cStart]]
        # 定义四个方向：东、南、西、北
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 当前方向索引，从东开始
        dir_idx = 0
        # 当前步长
        step = 1
        # 当前位置
        r, c = rStart, cStart
        # 总格子数
        total_cells = rows * cols
        
        # 当访问的格子数未达到总数时继续
        while len(result) < total_cells:
            # 每个步长走两次（螺旋特性）
            for _ in range(2):
                # 当前方向
                dr, dc = directions[dir_idx]
                # 走step步
                for _ in range(step):
                    # 更新位置
                    r += dr
                    c += dc
                    # 检查是否在网格内
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        # 如果已经访问完所有格子，提前返回
                        if len(result) == total_cells:
                            return result
                # 改变方向
                dir_idx = (dir_idx + 1) % 4
            # 增加步长
            step += 1
        
        return result
