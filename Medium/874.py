class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 定义方向向量：北、东、南、西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 初始方向索引，0表示面向北方
        direction_index = 0
        # 初始位置
        x, y = 0, 0
        # 将障碍物转换为集合以提高查找效率
        obstacles_set = set(map(tuple, obstacles))
        # 记录最大距离平方
        max_distance_sq = 0
        
        for cmd in commands:
            if cmd == -2:  # 左转90度
                direction_index = (direction_index - 1) % 4
            elif cmd == -1:  # 右转90度
                direction_index = (direction_index + 1) % 4
            else:  # 向前移动1-9个单位
                dx, dy = directions[direction_index]
                for _ in range(cmd):
                    next_x = x + dx
                    next_y = y + dy
                    # 如果下一个位置有障碍物，停止移动
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                    # 更新最大距离平方
                    max_distance_sq = max(max_distance_sq, x*x + y*y)
        
        return max_distance_sq
