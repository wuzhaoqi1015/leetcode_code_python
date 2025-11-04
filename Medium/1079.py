class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        
        # 使用集合存储所有可能的非空排列
        res = set()
        
        # 生成所有可能的排列，长度从1到tiles长度
        for i in range(1, len(tiles) + 1):
            # 生成长度为i的所有排列
            for perm in permutations(tiles, i):
                # 将排列转换为字符串并加入集合
                res.add(''.join(perm))
        
        # 返回集合大小，即不同非空序列的数量
        return len(res)
