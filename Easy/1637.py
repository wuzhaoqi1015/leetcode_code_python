class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 提取所有点的x坐标
        x_coords = [point[0] for point in points]
        
        # 对x坐标进行排序
        x_coords.sort()
        
        max_width = 0
        
        # 遍历相邻的x坐标，计算宽度差
        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i-1]
            if width > max_width:
                max_width = width
                
        return max_width
