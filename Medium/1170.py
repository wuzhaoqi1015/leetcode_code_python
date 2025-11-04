class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 定义辅助函数计算字符串中最小字母的出现频次
        def f(s: str) -> int:
            if not s:
                return 0
            min_char = min(s)  # 找到字典序最小的字符
            return s.count(min_char)  # 统计最小字符的出现次数
        
        # 预处理words中每个单词的f值
        word_freqs = []
        for word in words:
            word_freqs.append(f(word))
        
        # 对word_freqs进行排序以便后续二分查找
        word_freqs.sort()
        
        answer = []
        n = len(word_freqs)
        
        # 对每个查询进行处理
        for query in queries:
            query_freq = f(query)
            # 使用二分查找找到第一个大于query_freq的位置
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if word_freqs[mid] <= query_freq:
                    left = mid + 1
                else:
                    right = mid
            # 计算满足条件的单词数量
            count = n - left
            answer.append(count)
        
        return answer
