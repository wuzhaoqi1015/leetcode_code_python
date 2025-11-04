class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x = 1
        y = 1000
        # 使用双指针方法，从矩阵的右上角开始搜索
        while x <= 1000 and y >= 1:
            current = customfunction.f(x, y)
            if current == z:
                result.append([x, y])
                x += 1
                y -= 1
            elif current < z:
                # 如果当前值小于z，需要增加x来增大函数值
                x += 1
            else:
                # 如果当前值大于z，需要减小y来减小函数值
                y -= 1
        return result
