class WordDictionary:
    def __init__(self):
        # 使用字典实现前缀树结构
        self.trie = {}

    def addWord(self, word: str) -> None:
        # 遍历单词的每个字符，构建前缀树
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        # 在单词结尾标记结束
        node['#'] = True

    def search(self, word: str) -> bool:
        # 使用DFS递归搜索，处理通配符情况
        def dfs(index, node):
            # 遍历到单词末尾
            if index == len(word):
                return '#' in node
            char = word[index]
            # 如果是普通字符
            if char != '.':
                if char not in node:
                    return False
                return dfs(index + 1, node[char])
            # 如果是通配符，遍历所有可能的子节点
            for child in node:
                if child != '#' and dfs(index + 1, node[child]):
                    return True
            return False

        return dfs(0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
