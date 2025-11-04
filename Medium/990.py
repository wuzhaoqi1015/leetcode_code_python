class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # 初始化并查集，26个小写字母
        parent = list(range(26))
        
        def find(x):
            # 路径压缩
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # 合并两个集合
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # 第一遍处理所有等式，建立连通关系
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)
        
        # 第二遍检查所有不等式
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                # 如果不相等的两个变量在同一个连通分量中，则矛盾
                if find(x) == find(y):
                    return False
        
        return True
