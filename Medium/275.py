class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        # 使用二分查找来满足对数时间复杂度要求
        while left <= right:
            mid = left + (right - left) // 2
            # 计算当前中点对应的论文数量
            papers = n - mid
            # 如果当前引用次数大于等于论文数量，说明满足h指数条件
            if citations[mid] >= papers:
                # 继续向左查找可能更大的h指数
                right = mid - 1
            else:
                # 否则向右查找
                left = mid + 1
        # 最终left指向第一个满足条件的索引，h指数为n - left
        return n - left
