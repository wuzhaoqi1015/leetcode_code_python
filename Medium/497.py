import random
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # 计算每个矩形包含的整数点数量
        self.areas = []
        total = 0
        for rect in rects:
            a, b, x, y = rect
            # 计算矩形中的整数点数量（包含边界）
            points = (x - a + 1) * (y - b + 1)
            total += points
            self.areas.append(total)
        self.total_points = total

    def pick(self) -> List[int]:
        # 随机选择一个点索引
        rand_point = random.randint(0, self.total_points - 1)
        
        # 找到对应的矩形
        left, right = 0, len(self.areas) - 1
        while left < right:
            mid = (left + right) // 2
            if rand_point < self.areas[mid]:
                right = mid
            else:
                left = mid + 1
        
        rect_idx = left
        # 计算在该矩形中的偏移量
        if rect_idx == 0:
            offset = rand_point
        else:
            offset = rand_point - self.areas[rect_idx - 1]
        
        # 计算具体坐标
        a, b, x, y = self.rects[rect_idx]
        width = x - a + 1
        # 计算行和列
        row = offset // width
        col = offset % width
        
        return [a + col, b + row]
