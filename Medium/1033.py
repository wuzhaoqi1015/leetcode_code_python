class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # 将三个位置排序
        positions = sorted([a, b, c])
        x, y, z = positions[0], positions[1], positions[2]
        
        # 计算最大移动次数：每次移动可以填补一个空位
        # 最大移动次数等于两端石子之间的空位数
        max_moves = (z - x - 2)
        
        # 计算最小移动次数
        # 情况1：如果三个位置已经连续，不需要移动
        if z - x == 2:
            min_moves = 0
        # 情况2：如果任意两个位置相邻或只有一个空位，只需要一次移动
        elif (y - x <= 2) or (z - y <= 2):
            min_moves = 1
        # 情况3：其他情况需要两次移动
        else:
            min_moves = 2
            
        return [min_moves, max_moves]
