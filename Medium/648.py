class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 构建前缀树节点类
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False
        
        # 构建前缀树
        root = TrieNode()
        # 将词根按长度排序，确保遇到相同前缀时选择最短的
        dictionary.sort(key=len)
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        # 分割句子为单词列表
        words = sentence.split()
        result = []
        
        # 对每个单词进行词根替换
        for word in words:
            node = root
            replacement = []
            found = False
            # 在前缀树中查找最短词根
            for char in word:
                if char not in node.children:
                    break
                node = node.children[char]
                replacement.append(char)
                # 找到词根则立即使用
                if node.is_end:
                    found = True
                    break
            # 如果找到词根则使用词根，否则使用原单词
            result.append(''.join(replacement) if found else word)
        
        # 将结果列表连接成字符串返回
        return ' '.join(result)
