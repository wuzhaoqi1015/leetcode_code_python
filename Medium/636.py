class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n  # 初始化结果数组，每个函数的独占时间初始为0
        stack = []  # 使用栈来跟踪当前执行的函数
        prev_time = 0  # 记录上一个事件的时间戳
        
        for log in logs:
            parts = log.split(':')  # 分割日志字符串
            func_id = int(parts[0])  # 提取函数ID
            status = parts[1]  # 提取状态（start或end）
            curr_time = int(parts[2])  # 提取当前时间戳
            
            if status == 'start':
                if stack:
                    # 如果栈不为空，当前正在执行的函数需要记录从prev_time到curr_time-1的时间
                    result[stack[-1]] += curr_time - prev_time
                stack.append(func_id)  # 将当前函数ID压入栈
                prev_time = curr_time  # 更新prev_time为当前时间戳
            else:
                # 处理end状态，栈顶元素应为当前结束的函数
                result[stack.pop()] += curr_time - prev_time + 1  # 结束时间包含当前时间戳，所以加1
                prev_time = curr_time + 1  # 更新prev_time为下一个时间单位
        
        return result
