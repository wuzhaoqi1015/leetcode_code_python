from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(k):
            i, j = 0, 0
            m, n = len(nums1), len(nums2)
            while True:
                if i >= m:
                    return nums2[j + k - 1]
                if j >= n:
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])
                new_i = i + k // 2 - 1
                new_j = j + k // 2 - 1
                val_i = nums1[new_i] if new_i < m else float('inf')
                val_j = nums2[new_j] if new_j < n else float('inf')
                if val_i <= val_j:
                    i += k // 2
                    k -= k // 2
                else:
                    j += k // 2
                    k -= k // 2

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return get_kth(total // 2 + 1)
        else:
            return (get_kth(total // 2) + get_kth(total // 2 + 1)) / 2.0
