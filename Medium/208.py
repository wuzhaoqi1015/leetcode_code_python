class Trie:

    def __init__(self):
        # 初始化根节点，使用字典存储子节点
        self.children = {}
        # 标记当前节点是否为单词结尾
        self.is_end = False

    def insert(self, word: str) -> None:
        # 从根节点开始
        node = self
        # 遍历单词中的每个字符
        for char in word:
            # 如果字符不在当前节点的子节点中，创建新的子节点
            if char not in node.children:
                node.children[char] = Trie()
            # 移动到下一个节点
            node = node.children[char]
        # 标记单词结束
        node.is_end = True

    def search(self, word: str) -> bool:
        # 从根节点开始
        node = self
        # 遍历单词中的每个字符
        for char in word:
            # 如果字符不在当前节点的子节点中，返回False
            if char not in node.children:
                return False
            # 移动到下一个节点
            node = node.children[char]
        # 检查是否到达单词结尾
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # 从根节点开始
        node = self
        # 遍历前缀中的每个字符
        for char in prefix:
            # 如果字符不在当前节点的子节点中，返回False
            if char not in node.children:
                return False
            # 移动到下一个节点
            node = node.children[char]
        # 前缀存在
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
