class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用集合操作求交集，自动去重
        set1 = set(nums1)
        set2 = set(nums2)
        # 返回两个集合的交集
        return list(set1 & set2)
