class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        
        radiant_queue = deque()
        dire_queue = deque()
        
        # 初始化两个队列，存储参议员的索引位置
        for idx, senator in enumerate(senate):
            if senator == 'R':
                radiant_queue.append(idx)
            else:
                dire_queue.append(idx)
        
        n = len(senate)
        
        # 模拟投票过程，直到某一方队列为空
        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()
            
            # 索引较小的参议员可以禁止对方参议员的权利
            if radiant_index < dire_index:
                # Radiant参议员禁止Dire参议员，并将自己加入下一轮
                radiant_queue.append(radiant_index + n)
            else:
                # Dire参议员禁止Radiant参议员，并将自己加入下一轮
                dire_queue.append(dire_index + n)
        
        # 根据最终哪个队列非空判断获胜方
        return "Radiant" if radiant_queue else "Dire"
