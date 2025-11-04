class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 按单词长度排序，便于处理
        words.sort(key=len)
        dp = {}  # 存储每个单词的最长链长度
        
        max_chain = 1
        for word in words:
            dp[word] = 1  # 每个单词至少可以形成长度为1的链
            
            # 尝试删除每个位置的字符，检查是否存在前身
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  # 删除第i个字符
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            
            max_chain = max(max_chain, dp[word])
        
        return max_chain
