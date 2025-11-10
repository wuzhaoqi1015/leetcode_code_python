class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 创建分数到原始索引的映射
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        # 按分数降序排序
        indexed_scores.sort(key=lambda x: x[0], reverse=True)
        
        # 初始化结果列表
        result = [""] * len(score)
        
        # 分配奖牌和名次
        for rank, (s, idx) in enumerate(indexed_scores):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
                
        return result
