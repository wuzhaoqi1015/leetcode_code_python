class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 使用集合存储字符串中出现的所有字母
        char_set = set()
        # 遍历字符串中的每个字符
        for char in sentence:
            char_set.add(char)
            # 如果集合大小达到26，说明已包含所有字母，可提前结束
            if len(char_set) == 26:
                return True
        # 检查集合大小是否为26
        return len(char_set) == 26
