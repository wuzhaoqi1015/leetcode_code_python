class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0
            
        result = 0
        # 遍历每个点作为中心点i
        for i in range(n):
            distance_count = {}
            # 计算其他所有点到点i的距离
            for j in range(n):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx * dx + dy * dy  # 使用平方距离避免浮点数运算
                
                if dist in distance_count:
                    distance_count[dist] += 1
                else:
                    distance_count[dist] = 1
            
            # 对于每个距离，如果有m个点与i距离相同
            # 则从这m个点中选2个点的排列数为m*(m-1)
            for count in distance_count.values():
                if count >= 2:
                    result += count * (count - 1)
        
        return result
