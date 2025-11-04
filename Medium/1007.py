class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # 检查是否能让所有骨牌的上半部分或下半部分都变成目标数字
        def check(target):
            rotations_top = 0  # 需要旋转多少次让上半部分变成target
            rotations_bottom = 0  # 需要旋转多少次让下半部分变成target
            
            for i in range(len(tops)):
                # 如果当前骨牌的两面都不包含目标数字，则不可能完成
                if tops[i] != target and bottoms[i] != target:
                    return -1
                # 如果上半部分不是目标数字，需要旋转（此时下半部分一定是目标数字）
                elif tops[i] != target:
                    rotations_top += 1
                # 如果下半部分不是目标数字，需要旋转（此时上半部分一定是目标数字）
                elif bottoms[i] != target:
                    rotations_bottom += 1
            
            # 返回两种方案中旋转次数较少的
            return min(rotations_top, rotations_bottom)
        
        # 尝试第一个骨牌的两个数字作为候选目标
        result1 = check(tops[0])
        result2 = check(bottoms[0])
        
        # 如果第一个候选目标可行，返回结果；否则尝试第二个候选目标
        if result1 != -1:
            return result1
        elif result2 != -1:
            return result2
        else:
            return -1
