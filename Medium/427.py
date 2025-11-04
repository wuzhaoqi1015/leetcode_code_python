class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r_start, r_end, c_start, c_end):
            # 检查当前区域是否所有值相同
            all_same = True
            first_val = grid[r_start][c_start]
            for i in range(r_start, r_end):
                for j in range(c_start, c_end):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            # 如果所有值相同，创建叶子节点
            if all_same:
                return Node(first_val == 1, True, None, None, None, None)
            
            # 如果值不同，创建非叶子节点并递归处理四个子区域
            r_mid = (r_start + r_end) // 2
            c_mid = (c_start + c_end) // 2
            
            top_left = dfs(r_start, r_mid, c_start, c_mid)
            top_right = dfs(r_start, r_mid, c_mid, c_end)
            bottom_left = dfs(r_mid, r_end, c_start, c_mid)
            bottom_right = dfs(r_mid, r_end, c_mid, c_end)
            
            # 非叶子节点的val可以任意设置，这里设为True
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
        
        n = len(grid)
        return dfs(0, n, 0, n)
