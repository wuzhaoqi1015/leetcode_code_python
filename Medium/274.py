class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 对引用次数进行降序排序
        citations.sort(reverse=True)
        n = len(citations)
        h = 0
        
        # 遍历排序后的引用次数
        for i in range(n):
            # 当前论文的引用次数
            current_citation = citations[i]
            # 当前有 i+1 篇论文引用次数 >= current_citation
            # 但我们需要找到最大的 h 使得至少有 h 篇论文引用次数 >= h
            if current_citation >= i + 1:
                h = i + 1
            else:
                # 一旦不满足条件，就可以提前结束
                break
                
        return h
