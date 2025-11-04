class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 创建最大覆盖数组，记录每个起点能到达的最远位置
        max_reach = [0] * (time + 1)
        
        # 填充max_reach数组
        for start, end in clips:
            if start <= time:
                # 只考虑在time范围内的起点
                max_reach[start] = max(max_reach[start], end)
        
        # 初始化变量
        current_end = 0  # 当前已覆盖的最远位置
        next_end = 0     # 下一段能到达的最远位置
        count = 0        # 片段计数
        
        # 遍历每个位置
        for i in range(time + 1):
            # 更新下一段能到达的最远位置
            next_end = max(next_end, max_reach[i])
            
            # 如果当前位置等于当前已覆盖的最远位置
            if i == current_end:
                # 如果已经到达目标时间，返回片段数量
                if i == time:
                    return count
                # 如果下一段无法延伸得更远，说明无法覆盖
                if next_end <= i:
                    return -1
                # 选择新的片段，更新当前覆盖范围
                current_end = next_end
                count += 1
                # 如果已经覆盖到目标时间，提前返回
                if current_end >= time:
                    return count
        
        # 如果循环结束仍未覆盖到目标时间，返回-1
        return -1
