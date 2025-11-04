class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        
        # 并查集查找函数
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 并查集合并函数
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        # 根据pairs建立连通关系
        for a, b in pairs:
            union(a, b)
        
        # 将同一连通分量的索引分组
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)
        
        # 对每个连通分量内的字符进行排序
        result = list(s)
        for indices in groups.values():
            # 获取当前连通分量的所有字符
            chars = [result[i] for i in indices]
            # 对字符按字典序排序
            chars.sort()
            # 对索引按升序排序
            indices.sort()
            # 将排序后的字符放回对应位置
            for idx, char in zip(indices, chars):
                result[idx] = char
        
        return ''.join(result)
