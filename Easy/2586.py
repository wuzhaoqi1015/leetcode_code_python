class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # 定义元音字母集合
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        # 遍历指定范围内的字符串
        for i in range(left, right + 1):
            word = words[i]
            # 检查字符串是否非空且首尾都是元音
            if word and word[0] in vowels and word[-1] in vowels:
                count += 1
        return count
