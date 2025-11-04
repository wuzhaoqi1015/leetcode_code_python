class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 如果字符串长度小于等于10，直接返回空列表
        if len(s) <= 10:
            return []
        
        # 使用字典记录每个长度为10的子串出现的次数
        seq_count = {}
        result = []
        
        # 遍历所有可能的长度为10的子串
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            # 更新子串计数
            seq_count[substring] = seq_count.get(substring, 0) + 1
            # 当计数达到2时加入结果，避免重复添加
            if seq_count[substring] == 2:
                result.append(substring)
        
        return result
