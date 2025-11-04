class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # 定义一个函数来生成特殊等价字符串的规范表示
        def get_signature(word):
            # 分离奇数下标和偶数下标的字符
            odd_chars = []
            even_chars = []
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even_chars.append(char)
                else:
                    odd_chars.append(char)
            # 对奇数下标和偶数下标的字符分别排序
            odd_chars.sort()
            even_chars.sort()
            # 返回排序后的组合作为签名
            return ''.join(even_chars) + ''.join(odd_chars)
        
        # 使用集合来存储不同的签名
        signature_set = set()
        # 遍历每个单词，计算其签名并加入集合
        for word in words:
            sig = get_signature(word)
            signature_set.add(sig)
        # 返回集合的大小，即不同特殊等价组的数量
        return len(signature_set)
