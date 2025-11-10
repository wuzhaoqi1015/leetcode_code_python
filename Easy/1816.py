class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # 将句子按空格分割成单词列表
        words = s.split()
        # 取前k个单词
        truncated_words = words[:k]
        # 用空格连接单词并返回
        return ' '.join(truncated_words)
