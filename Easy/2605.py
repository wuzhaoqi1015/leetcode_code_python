class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # 将数组转换为集合以便快速查找
        set1 = set(nums1)
        set2 = set(nums2)
        
        # 查找两个集合的交集，即同时出现在两个数组中的数字
        common = set1 & set2
        if common:
            # 如果存在共同数字，返回最小的共同数字
            return min(common)
        
        # 如果没有共同数字，找到两个数组各自的最小值
        min1 = min(nums1)
        min2 = min(nums2)
        
        # 返回由两个最小值组成的最小两位数
        # 通过比较确保较小的数字在前
        if min1 < min2:
            return min1 * 10 + min2
        else:
            return min2 * 10 + min1
