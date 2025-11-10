class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串按空格分割成单词列表
        words = s.split(' ')
        # 对每个单词进行反转
        reversed_words = [word[::-1] for word in words]
        # 将反转后的单词用空格连接成字符串
        return ' '.join(reversed_words)
