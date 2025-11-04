from collections import defaultdict, deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 构建员工到下属的映射关系
        subordinates = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        
        # 使用BFS计算最大通知时间
        queue = deque()
        queue.append((headID, 0))  # (当前员工ID, 累计通知时间)
        max_time = 0
        
        while queue:
            current_employee, current_time = queue.popleft()
            # 更新最大通知时间
            max_time = max(max_time, current_time)
            
            # 遍历当前员工的所有下属
            for subordinate in subordinates[current_employee]:
                # 下属的累计通知时间 = 当前累计时间 + 当前员工通知下属所需时间
                queue.append((subordinate, current_time + informTime[current_employee]))
        
        return max_time
