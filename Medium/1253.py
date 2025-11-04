class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        # 初始化结果矩阵
        row0 = [0] * n
        row1 = [0] * n
        
        # 首先处理colsum为2的列，这些列必须两行都为1
        for i in range(n):
            if colsum[i] == 2:
                row0[i] = 1
                row1[i] = 1
                upper -= 1
                lower -= 1
        
        # 检查是否出现负数，如果出现说明不可能
        if upper < 0 or lower < 0:
            return []
        
        # 处理colsum为1的列，优先分配给row0直到upper用完，然后分配给row1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    row0[i] = 1
                    upper -= 1
                else:
                    row1[i] = 1
                    lower -= 1
        
        # 最终检查upper和lower是否都为0，且所有列的和都满足
        if upper == 0 and lower == 0:
            return [row0, row1]
        else:
            return []
