class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # 初始化结果数组，默认值为0
        stack = []  # 使用单调栈存储温度索引，栈中温度递减
        
        for i in range(n):
            # 当栈不为空且当前温度大于栈顶索引对应的温度时
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  # 弹出栈顶索引
                answer[prev_index] = i - prev_index  # 计算天数差
            stack.append(i)  # 将当前索引入栈
            
        return answer
