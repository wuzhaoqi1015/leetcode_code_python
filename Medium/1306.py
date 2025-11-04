from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n  # 记录访问过的位置，避免重复访问
        
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            current = queue.popleft()
            
            # 如果当前位置值为0，返回True
            if arr[current] == 0:
                return True
            
            # 向右跳转
            right_pos = current + arr[current]
            if 0 <= right_pos < n and not visited[right_pos]:
                visited[right_pos] = True
                queue.append(right_pos)
            
            # 向左跳转
            left_pos = current - arr[current]
            if 0 <= left_pos < n and not visited[left_pos]:
                visited[left_pos] = True
                queue.append(left_pos)
        
        # 如果所有可达位置都访问过且没有找到值为0的位置，返回False
        return False
