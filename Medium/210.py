from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建邻接表和入度数组
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # 构建图结构
        for course, pre in prerequisites:
            graph[pre].append(course)  # 先修课程指向后续课程
            in_degree[course] += 1     # 后续课程的入度加1
        
        # 初始化队列，将所有入度为0的课程加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 拓扑排序结果列表
        result = []
        
        # 开始拓扑排序
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # 遍历当前课程的所有后续课程
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1  # 减少后续课程的入度
                if in_degree[neighbor] == 0:  # 如果入度变为0，加入队列
                    queue.append(neighbor)
        
        # 检查是否所有课程都被安排
        if len(result) == numCourses:
            return result
        else:
            return []
