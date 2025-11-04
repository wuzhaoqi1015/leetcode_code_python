class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 初始位置和方向
        x, y = 0, 0
        # 方向向量：北、东、南、西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 初始方向索引，0表示北
        dir_idx = 0
        
        # 执行一轮指令
        for cmd in instructions:
            if cmd == 'G':
                # 朝当前方向移动
                dx, dy = directions[dir_idx]
                x += dx
                y += dy
            elif cmd == 'L':
                # 左转，方向索引减1（逆时针）
                dir_idx = (dir_idx - 1) % 4
            elif cmd == 'R':
                # 右转，方向索引加1（顺时针）
                dir_idx = (dir_idx + 1) % 4
        
        # 检查是否形成环的条件：
        # 1. 回到原点，无论方向如何都会形成环
        # 2. 没有回到原点但方向改变了（不是朝北），经过多轮执行后最终会形成环
        return (x == 0 and y == 0) or dir_idx != 0
