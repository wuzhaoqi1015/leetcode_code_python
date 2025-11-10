class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # 创建一个字典来记录每个字符第一次出现的位置
        first_occurrence = {}
        
        # 遍历字符串中的每个字符
        for idx, char in enumerate(s):
            # 如果字符已经在字典中，说明这是第二次出现
            if char in first_occurrence:
                # 计算两次出现之间的字母数量（不包含两个端点）
                actual_distance = idx - first_occurrence[char] - 1
                # 获取该字符对应的距离索引
                char_index = ord(char) - ord('a')
                # 检查实际距离是否与distance数组中对应位置的值相等
                if actual_distance != distance[char_index]:
                    return False
            else:
                # 如果是第一次出现，记录位置
                first_occurrence[char] = idx
        
        # 所有字符的距离检查都通过，返回True
        return True
