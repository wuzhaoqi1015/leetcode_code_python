class Solution:
    def reorganizeString(self, s: str) -> str:
        # 统计每个字符的出现频率
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # 找到出现次数最多的字符及其频率
        max_char = max(freq, key=freq.get)
        max_count = freq[max_char]
        
        # 如果最大频率超过总长度的一半（向上取整），则无法满足条件
        if max_count > (len(s) + 1) // 2:
            return ""
        
        # 初始化结果列表，长度为原字符串长度
        res = [''] * len(s)
        
        # 先填充偶数位置（0, 2, 4, ...）
        index = 0
        while freq[max_char] > 0:
            res[index] = max_char
            freq[max_char] -= 1
            index += 2
        
        # 填充剩余字符到剩余位置
        for char, count in freq.items():
            while count > 0:
                # 如果偶数位置填满了，从奇数位置开始
                if index >= len(s):
                    index = 1
                res[index] = char
                count -= 1
                index += 2
        
        # 将列表转换为字符串返回
        return ''.join(res)
