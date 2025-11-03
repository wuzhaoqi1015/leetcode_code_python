class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 使用动态规划，dp[i]表示s的前i个字符能否被拆分成字典中的单词
        word_set = set(wordDict)  # 转换为集合提高查找效率
        n = len(s)
        dp = [False] * (n + 1)   # 初始化dp数组
        dp[0] = True             # 空字符串可以被拆分
        
        # 遍历字符串的每个位置
        for i in range(1, n + 1):
            # 检查所有可能的分割点
            for j in range(i):
                # 如果前j个字符可以拆分，且s[j:i]在字典中
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一个有效拆分即可
        
        return dp[n]
