class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 使用栈模拟操作过程
        stack = []
        pop_index = 0  # 指向popped序列当前需要弹出的元素
        
        # 遍历pushed序列中的每个元素
        for num in pushed:
            # 将当前元素压入栈中
            stack.append(num)
            
            # 当栈不为空且栈顶元素等于popped序列当前需要弹出的元素时
            while stack and stack[-1] == popped[pop_index]:
                # 弹出栈顶元素
                stack.pop()
                # 移动到popped序列的下一个元素
                pop_index += 1
        
        # 如果所有元素都能按顺序弹出，则栈应该为空
        return not stack
