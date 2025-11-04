import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # 使用极坐标变换方法生成均匀分布的点
        # 首先生成均匀的半径分布（注意需要开方来保证均匀性）
        r = self.radius * math.sqrt(random.random())
        # 生成均匀的角度分布
        theta = random.uniform(0, 2 * math.pi)
        # 转换为直角坐标系并加上圆心偏移
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]
