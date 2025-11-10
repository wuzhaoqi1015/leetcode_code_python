class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用单调栈预处理nums2中每个元素的下一个更大元素
        stack = []
        next_greater = {}
        
        # 从右往左遍历nums2，维护单调递减栈
        for num in reversed(nums2):
            # 弹出栈顶所有小于等于当前元素的元素
            while stack and stack[-1] <= num:
                stack.pop()
            # 如果栈不为空，栈顶元素就是当前元素的下一个更大元素
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            # 将当前元素压入栈中
            stack.append(num)
        
        # 对于nums1中的每个元素，直接从哈希表中获取结果
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result
