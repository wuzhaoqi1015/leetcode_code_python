class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        # 检查target是否存在于words中
        if target not in words:
            return -1
        
        min_distance = float('inf')
        # 遍历所有位置，找到所有等于target的索引
        for i in range(n):
            if words[i] == target:
                # 计算正向距离
                forward_dist = abs(i - startIndex)
                # 计算反向距离（考虑环形数组）
                backward_dist = n - forward_dist
                # 取两个方向中的较小值
                current_min = min(forward_dist, backward_dist)
                # 更新全局最小值
                if current_min < min_distance:
                    min_distance = current_min
        
        return min_distance
