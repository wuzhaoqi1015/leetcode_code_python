class Solution:
    def frequencySort(self, s: str) -> str:
        # 统计每个字符的频率
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        
        # 将字典项转换为列表并按频率降序排序
        sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        
        # 构建结果字符串
        result = []
        for char, count in sorted_items:
            result.append(char * count)
        
        return ''.join(result)
