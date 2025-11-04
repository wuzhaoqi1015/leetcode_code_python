class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 计算玩家到目标点的曼哈顿距离
        player_distance = abs(target[0]) + abs(target[1])
        
        # 检查每个阻碍者是否能比玩家更快到达目标点
        for ghost in ghosts:
            # 计算阻碍者到目标点的曼哈顿距离
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            # 如果阻碍者到目标点的距离小于等于玩家到目标点的距离
            # 则阻碍者可以在玩家到达目标点之前或同时到达
            if ghost_distance <= player_distance:
                return False
        
        # 如果所有阻碍者都无法在玩家之前到达目标点，则逃脱成功
        return True
