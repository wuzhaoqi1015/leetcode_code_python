class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 使用字典记录每个缝隙位置出现的次数
        gap_count = {}
        
        # 遍历每一行砖块
        for row in wall:
            # 当前行的累计宽度
            current_sum = 0
            # 遍历当前行的每一块砖（除了最后一块）
            for i in range(len(row) - 1):
                current_sum += row[i]
                # 记录缝隙位置出现的次数
                gap_count[current_sum] = gap_count.get(current_sum, 0) + 1
        
        # 如果没有找到任何缝隙，则线必须穿过所有行
        if not gap_count:
            return len(wall)
        
        # 找到出现次数最多的缝隙位置
        max_gap = max(gap_count.values())
        
        # 最少穿过的砖块数量 = 总行数 - 最多缝隙位置出现的次数
        return len(wall) - max_gap
