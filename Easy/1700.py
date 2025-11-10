from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 使用队列模拟学生排队过程
        from collections import deque
        student_queue = deque(students)
        sandwich_stack = sandwiches
        
        # 记录连续不匹配的次数，避免无限循环
        consecutive_failures = 0
        
        while student_queue and consecutive_failures < len(student_queue):
            # 检查队首学生是否喜欢栈顶三明治
            if student_queue[0] == sandwich_stack[0]:
                # 学生拿走三明治，从队列和栈中移除
                student_queue.popleft()
                sandwich_stack.pop(0)
                # 重置连续失败计数
                consecutive_failures = 0
            else:
                # 学生回到队列尾部
                student = student_queue.popleft()
                student_queue.append(student)
                # 增加连续失败计数
                consecutive_failures += 1
        
        # 剩余在队列中的学生就是无法吃到午餐的学生
        return len(student_queue)
