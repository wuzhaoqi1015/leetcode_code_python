class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # 将字母转换为对应的数字值
        def word_to_num(word):
            num_str = ''.join(str(ord(char) - ord('a')) for char in word)
            return int(num_str) if num_str else 0  # 处理空字符串情况
        
        # 计算三个单词的数值
        first_num = word_to_num(firstWord)
        second_num = word_to_num(secondWord)
        target_num = word_to_num(targetWord)
        
        # 检查前两个单词的和是否等于目标单词的数值
        return first_num + second_num == target_num
