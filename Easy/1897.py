class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # 统计所有字符的总出现次数
        total_chars = sum(len(word) for word in words)
        n = len(words)
        
        # 如果总字符数不能被字符串数量整除，不可能平均分配
        if total_chars % n != 0:
            return False
            
        # 统计所有字符的频率
        freq = {}
        for word in words:
            for char in word:
                freq[char] = freq.get(char, 0) + 1
                
        # 检查每个字符的频率是否能被n整除
        for count in freq.values():
            if count % n != 0:
                return False
                
        return True
