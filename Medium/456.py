class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 维护一个单调递减栈，存储可能的"2"元素
        stack = []
        # 记录当前元素左边的最小值，作为可能的"1"元素
        min_left = [0] * n
        min_left[0] = nums[0]
        
        # 预处理每个位置左边的最小值
        for i in range(1, n):
            min_left[i] = min(min_left[i-1], nums[i])
        
        # 从右向左遍历，寻找满足条件的"3"和"2"
        for j in range(n-1, -1, -1):
            if nums[j] > min_left[j]:  # 确保存在比当前左边最小值大的元素
                # 维护单调栈，弹出所有小于等于左边最小值的元素
                while stack and stack[-1] <= min_left[j]:
                    stack.pop()
                # 如果栈顶元素小于当前元素，说明找到了132模式
                if stack and stack[-1] < nums[j]:
                    return True
                # 将当前元素压入栈中
                stack.append(nums[j])
        
        return False
