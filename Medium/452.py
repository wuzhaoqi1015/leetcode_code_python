class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        # 按右边界升序排序
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        # 遍历所有区间
        for i in range(1, len(points)):
            # 如果当前气球的左边界大于当前箭的位置，需要新的箭
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]
            # 否则当前箭可以射爆这个气球，继续检查下一个
        
        return arrows
