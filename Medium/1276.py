class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 设巨无霸汉堡数量为x，小皇堡数量为y
        # 根据题意可得方程组：
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        
        # 解方程组：
        # 从第二个方程得：y = cheeseSlices - x
        # 代入第一个方程：4x + 2(cheeseSlices - x) = tomatoSlices
        # 化简得：2x + 2cheeseSlices = tomatoSlices
        # 所以：x = (tomatoSlices - 2 * cheeseSlices) / 2
        
        # 计算巨无霸汉堡数量
        jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        
        # 检查解是否满足条件
        # 1. jumbo必须是整数
        # 2. jumbo必须非负
        # 3. 小皇堡数量必须非负
        if jumbo < 0 or jumbo != int(jumbo):
            return []
        
        jumbo = int(jumbo)
        small = cheeseSlices - jumbo
        
        # 检查小皇堡数量是否非负
        if small < 0:
            return []
        
        # 验证解是否正确
        if 4 * jumbo + 2 * small == tomatoSlices and jumbo + small == cheeseSlices:
            return [jumbo, small]
        else:
            return []
