class MagicDictionary:

    def __init__(self):
        # 初始化存储字典单词的集合
        self.words_set = set()

    def buildDict(self, dictionary: List[str]) -> None:
        # 将字典单词存入集合
        for word in dictionary:
            self.words_set.add(word)

    def search(self, searchWord: str) -> bool:
        # 遍历搜索单词的每个位置
        for i in range(len(searchWord)):
            # 获取当前位置的原始字符
            original_char = searchWord[i]
            # 尝试替换为其他25个小写字母
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # 跳过原始字符
                if c == original_char:
                    continue
                # 构建新单词
                new_word = searchWord[:i] + c + searchWord[i+1:]
                # 检查新单词是否在字典中
                if new_word in self.words_set:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
