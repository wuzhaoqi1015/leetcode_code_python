from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        # 记录已完成的课程数量
        completed = 0
        
        # 拓扑排序
        while queue:
            current = queue.popleft()
            completed += 1
            
            # 遍历当前课程的所有后续课程
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1  # 后续课程的入度减1
                if in_degree[neighbor] == 0:  # 如果入度变为0，加入队列
                    queue.append(neighbor)
        
        # 如果完成的课程数量等于总课程数，说明可以完成所有课程
        return completed == numCourses
