class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # 构建邻接表
        graph = [[] for _ in range(n)]
        for x, y in paths:
            # 将花园编号转换为0-based索引
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
        
        # 初始化结果数组，全部设为0表示未染色
        answer = [0] * n
        
        # 遍历每个花园进行染色
        for i in range(n):
            # 记录相邻花园已使用的颜色
            used_colors = set()
            # 遍历所有相邻花园，收集已使用的颜色
            for neighbor in graph[i]:
                if answer[neighbor] != 0:
                    used_colors.add(answer[neighbor])
            
            # 从1-4中选择第一个未被相邻花园使用的颜色
            for color in range(1, 5):
                if color not in used_colors:
                    answer[i] = color
                    break
        
        return answer
