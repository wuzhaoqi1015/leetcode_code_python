class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        # 记录img1和img2中所有1的位置
        pos1 = []
        pos2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    pos1.append((i, j))
                if img2[i][j] == 1:
                    pos2.append((i, j))
        
        # 使用字典记录所有可能的位移向量及其出现次数
        vector_count = {}
        max_overlap = 0
        
        # 对于img1中的每个1和img2中的每个1，计算位移向量
        for x1, y1 in pos1:
            for x2, y2 in pos2:
                vector = (x2 - x1, y2 - y1)  # 位移向量
                vector_count[vector] = vector_count.get(vector, 0) + 1
                max_overlap = max(max_overlap, vector_count[vector])
        
        return max_overlap
