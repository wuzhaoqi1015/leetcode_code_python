class MapSum:

    def __init__(self):
        self.children = {}  # 子节点字典
        self.value = 0      # 当前节点的值
        self.is_end = False # 标记是否为单词结尾

    def insert(self, key: str, val: int) -> None:
        node = self
        # 遍历键的每个字符
        for char in key:
            if char not in node.children:
                node.children[char] = MapSum()
            node = node.children[char]
        # 标记单词结尾并存储值
        node.is_end = True
        node.value = val

    def sum(self, prefix: str) -> int:
        node = self
        # 先定位到前缀的最后一个节点
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        # 从该节点开始DFS遍历所有子节点求和
        return self._dfs(node)
    
    def _dfs(self, node):
        total = 0
        # 如果当前节点是单词结尾，加上其值
        if node.is_end:
            total += node.value
        # 递归遍历所有子节点
        for child in node.children.values():
            total += self._dfs(child)
        return total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
