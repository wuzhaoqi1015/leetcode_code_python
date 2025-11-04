class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # 初始化结果数组，默认值为-1
        stack = []  # 单调栈，存储元素索引
        
        # 遍历两倍长度的数组模拟循环
        for i in range(2 * n):
            # 当前元素的真实索引
            idx = i % n
            # 当栈不为空且当前元素大于栈顶索引对应的元素时
            while stack and nums[idx] > nums[stack[-1]]:
                # 弹出栈顶索引，并更新该位置的下一个更大元素
                prev_idx = stack.pop()
                result[prev_idx] = nums[idx]
            # 只在第一轮遍历时压入索引，避免重复处理
            if i < n:
                stack.append(idx)
                
        return result
