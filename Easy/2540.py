class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # 使用双指针遍历两个有序数组
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        # 当两个指针都在数组范围内时循环
        while i < n1 and j < n2:
            # 如果当前元素相等，返回这个最小公共整数
            if nums1[i] == nums2[j]:
                return nums1[i]
            # 如果nums1当前元素较小，移动nums1的指针
            elif nums1[i] < nums2[j]:
                i += 1
            # 如果nums2当前元素较小，移动nums2的指针
            else:
                j += 1
        
        # 没有找到公共整数，返回-1
        return -1
