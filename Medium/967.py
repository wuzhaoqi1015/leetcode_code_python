class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 使用BFS方法生成所有符合条件的数字
        from collections import deque
        
        # 初始化队列，包含所有可能的起始数字（1-9，因为不能有前导0）
        queue = deque(range(1, 10))
        
        # 进行n-1次扩展，因为起始已经有一位数字
        for level in range(n - 1):
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                last_digit = current % 10  # 获取当前数字的最后一位
                
                # 生成下一个可能的数字
                next_digits = set()
                if last_digit + k <= 9:
                    next_digits.add(last_digit + k)
                if last_digit - k >= 0:
                    next_digits.add(last_digit - k)
                
                # 将新数字加入队列
                for digit in next_digits:
                    queue.append(current * 10 + digit)
        
        # 将队列转换为列表返回
        return list(queue)
