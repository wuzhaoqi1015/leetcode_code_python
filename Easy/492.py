class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 从平方根开始向下寻找最接近的宽度W
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        # 计算对应的长度L
        l = area // w
        return [l, w]
