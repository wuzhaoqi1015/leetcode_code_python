class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 计算第一个矩形的面积
        area_a = (ax2 - ax1) * (ay2 - ay1)
        # 计算第二个矩形的面积
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # 计算重叠部分的宽度
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        # 计算重叠部分的高度
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        # 计算重叠部分的面积
        overlap_area = overlap_width * overlap_height
        
        # 返回两个矩形总面积减去重叠部分面积
        return area_a + area_b - overlap_area
