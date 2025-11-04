class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # 过滤餐馆信息
        filtered = []
        for r in restaurants:
            # 检查素食友好过滤器
            if veganFriendly == 1 and r[2] == 0:
                continue
            # 检查价格过滤器
            if r[3] > maxPrice:
                continue
            # 检查距离过滤器
            if r[4] > maxDistance:
                continue
            # 符合条件的餐馆，记录id和rating用于排序
            filtered.append((r[0], r[1]))
        
        # 按rating降序排序，rating相同时按id降序排序
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        
        # 提取id列表
        result = [item[0] for item in filtered]
        return result
