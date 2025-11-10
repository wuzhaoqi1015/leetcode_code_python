class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # 将损坏的字母转换为集合，便于快速查找
        broken_set = set(brokenLetters)
        # 按空格分割文本得到单词列表
        words = text.split()
        count = 0  # 统计可以完整输入的单词数量
        
        # 遍历每个单词
        for word in words:
            # 检查单词中的每个字符
            can_type = True
            for char in word:
                # 如果字符在损坏集合中，标记为不可输入
                if char in broken_set:
                    can_type = False
                    break
            # 如果单词可以完整输入，计数加1
            if can_type:
                count += 1
                
        return count
