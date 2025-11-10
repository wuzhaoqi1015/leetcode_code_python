class Solution:
    def oddString(self, words: List[str]) -> str:
        # 计算每个单词的差值数组
        def get_diff_array(word):
            diff = []
            for i in range(len(word) - 1):
                # 计算相邻字符的差值
                diff.append(ord(word[i+1]) - ord(word[i]))
            return tuple(diff)  # 转换为元组以便作为字典键
        
        # 使用字典统计每个差值数组出现的次数
        diff_count = {}
        diff_to_word = {}  # 存储差值数组对应的单词
        
        for word in words:
            diff_array = get_diff_array(word)
            diff_count[diff_array] = diff_count.get(diff_array, 0) + 1
            diff_to_word[diff_array] = word
        
        # 找到出现次数为1的差值数组对应的单词
        for diff_array, count in diff_count.items():
            if count == 1:
                return diff_to_word[diff_array]
        
        return ""  # 理论上不会执行到这里，因为题目保证有且只有一个不同的字符串
