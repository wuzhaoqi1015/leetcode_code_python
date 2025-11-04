from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 使用深度优先搜索遍历所有可达房间
        n = len(rooms)
        visited = [False] * n  # 记录房间是否被访问过
        
        def dfs(room):
            # 标记当前房间为已访问
            visited[room] = True
            # 遍历当前房间中的所有钥匙
            for key in rooms[room]:
                # 如果钥匙对应的房间未被访问，则递归访问
                if not visited[key]:
                    dfs(key)
        
        # 从0号房间开始搜索
        dfs(0)
        
        # 检查是否所有房间都被访问过
        return all(visited)
