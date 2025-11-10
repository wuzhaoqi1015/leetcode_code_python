class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 初始化结果列表
        result = []
        # 获取两个字符串的最小长度
        min_len = min(len(word1), len(word2))
        
        # 交替添加字符直到较短字符串的末尾
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        # 添加较长字符串剩余的部分
        result.append(word1[min_len:])
        result.append(word2[min_len:])
        
        # 将列表转换为字符串返回
        return ''.join(result)
