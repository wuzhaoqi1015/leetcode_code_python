class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对nums1进行排序以便使用贪心策略
        sorted_nums1 = sorted(nums1)
        # 为nums2创建索引列表并按照值排序，保持原始索引信息
        sorted_nums2 = sorted([(val, idx) for idx, val in enumerate(nums2)])
        
        # 初始化结果列表和双指针
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        
        # 遍历排序后的nums2
        for num in sorted_nums1:
            # 如果当前nums1的值大于nums2当前最小值，则分配到对应位置
            if num > sorted_nums2[left][0]:
                res[sorted_nums2[left][1]] = num
                left += 1
            # 否则分配到nums2最大值的对应位置
            else:
                res[sorted_nums2[right][1]] = num
                right -= 1
        
        return res
