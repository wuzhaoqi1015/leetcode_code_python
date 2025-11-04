class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 使用单调栈存储可能作为坡起点的索引
        stack = []
        n = len(nums)
        # 构建单调递减栈，存储从左到右的递减序列索引
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        max_width = 0
        # 从右向左遍历，寻找最大宽度坡
        for j in range(n-1, -1, -1):
            # 当栈不为空且当前元素大于等于栈顶索引对应的元素时
            while stack and nums[j] >= nums[stack[-1]]:
                # 计算坡宽度并更新最大值
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
