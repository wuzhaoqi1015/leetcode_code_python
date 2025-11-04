class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 对牌组进行排序，得到递增顺序的卡牌值
        deck.sort()
        n = len(deck)
        # 初始化结果列表，长度与牌组相同，初始值设为0
        result = [0] * n
        # 使用双端队列模拟操作过程，队列中存储的是索引位置
        from collections import deque
        indices = deque(range(n))
        
        # 遍历排序后的牌组，按照模拟规则填充结果列表
        for card in deck:
            # 从队列左侧取出当前要显示的牌的位置
            idx = indices.popleft()
            # 将当前最小的牌放到该位置
            result[idx] = card
            # 如果队列中还有牌，将下一张牌移到队列末尾
            if indices:
                indices.append(indices.popleft())
        
        return result
