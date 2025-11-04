class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # 初始化并查集，每个字符的父节点初始化为自己
        parent = [i for i in range(26)]
        
        # 查找根节点的函数，带路径压缩
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 合并两个字符所在的集合，总是让字典序小的作为根节点
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a < root_b:
                parent[root_b] = root_a
            elif root_a > root_b:
                parent[root_a] = root_b
        
        # 遍历s1和s2，建立等价关系
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            union(idx1, idx2)
        
        # 构建结果字符串
        result = []
        for char in baseStr:
            idx = ord(char) - ord('a')
            root = find(idx)
            # 找到该字符所在集合的最小字符
            result.append(chr(root + ord('a')))
        
        return ''.join(result)
