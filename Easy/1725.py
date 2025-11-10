class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_side = 0
        count = 0
        for rect in rectangles:
            # 计算当前矩形能切出的最大正方形边长
            side = min(rect[0], rect[1])
            # 如果找到更大的边长，更新最大值并重置计数
            if side > max_side:
                max_side = side
                count = 1
            # 如果等于当前最大边长，增加计数
            elif side == max_side:
                count += 1
        return count
