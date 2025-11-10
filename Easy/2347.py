class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 检查是否为同花
        if len(set(suits)) == 1:
            return "Flush"
        
        # 统计每个点数的出现次数
        count = {}
        for rank in ranks:
            count[rank] = count.get(rank, 0) + 1
        
        # 检查是否有三条
        max_count = max(count.values())
        if max_count >= 3:
            return "Three of a Kind"
        
        # 检查是否有对子
        if max_count >= 2:
            return "Pair"
        
        # 否则为高牌
        return "High Card"
