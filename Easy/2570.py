class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # 使用双指针合并两个有序数组
        i, j = 0, 0
        result = []
        
        # 遍历两个数组直到其中一个遍历完成
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 == id2:
                # 当id相同时，合并值并添加到结果
                result.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                # 当nums1的id较小时，添加nums1的元素
                result.append([id1, val1])
                i += 1
            else:
                # 当nums2的id较小时，添加nums2的元素
                result.append([id2, val2])
                j += 1
        
        # 处理nums1剩余元素
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        # 处理nums2剩余元素
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        return result
