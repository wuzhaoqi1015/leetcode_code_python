class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # 创建集合存储那些正面和背面相同的数字，这些数字无论怎么翻转都会出现在正面
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        
        # 初始化结果为0，表示如果没有符合条件的数字就返回0
        result = 0
        
        # 遍历所有卡片的正面和背面数字
        for x in fronts + backs:
            # 如果当前数字不在same集合中，说明可以通过翻转避免它出现在正面
            if x not in same:
                # 如果result为0或者当前数字比result小，则更新result
                if result == 0 or x < result:
                    result = x
        
        return result
