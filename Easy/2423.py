class Solution:
    def equalFrequency(self, word: str) -> bool:
        # 统计每个字符的频率
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        
        # 尝试删除每个字符一次，检查剩余字符频率是否相同
        for char in word:
            # 临时减少当前字符的频率
            freq[char] -= 1
            
            # 如果频率为0，则从字典中移除该字符
            if freq[char] == 0:
                del freq[char]
            
            # 获取所有频率值
            frequencies = list(freq.values())
            
            # 检查所有频率是否相同
            if len(set(frequencies)) == 1:
                return True
            
            # 恢复原始频率
            freq[char] = freq.get(char, 0) + 1
        
        return False
