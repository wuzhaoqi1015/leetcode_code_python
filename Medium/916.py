class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # 计算words2中所有单词的字符最大频率需求
        max_freq = [0] * 26
        for word in words2:
            # 计算当前单词的字符频率
            curr_freq = [0] * 26
            for ch in word:
                curr_freq[ord(ch) - ord('a')] += 1
            # 更新最大频率需求
            for i in range(26):
                max_freq[i] = max(max_freq[i], curr_freq[i])
        
        result = []
        # 检查words1中的每个单词是否满足通用条件
        for word in words1:
            # 计算当前单词的字符频率
            word_freq = [0] * 26
            for ch in word:
                word_freq[ord(ch) - ord('a')] += 1
            
            # 检查是否满足所有字符频率需求
            is_universal = True
            for i in range(26):
                if word_freq[i] < max_freq[i]:
                    is_universal = False
                    break
            
            if is_universal:
                result.append(word)
        
        return result
