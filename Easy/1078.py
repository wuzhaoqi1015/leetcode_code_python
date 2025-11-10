class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # 将文本按空格分割成单词列表
        words = text.split()
        result = []
        # 遍历单词列表，检查每个可能的连续三个单词
        for i in range(len(words) - 2):
            # 如果当前单词匹配first且下一个单词匹配second，则添加第三个单词
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        return result
