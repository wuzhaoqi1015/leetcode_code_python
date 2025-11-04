from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 将死亡数字转换为集合以便快速查找
        dead_set = set(deadends)
        # 如果初始状态就是死亡数字，直接返回-1
        if "0000" in dead_set:
            return -1
        # 如果目标就是初始状态，直接返回0
        if target == "0000":
            return 0
        
        # 使用BFS队列，存储当前状态和步数
        queue = deque()
        queue.append(("0000", 0))
        # 记录已访问的状态
        visited = set()
        visited.add("0000")
        
        # BFS主循环
        while queue:
            current, steps = queue.popleft()
            
            # 如果找到目标状态，返回步数
            if current == target:
                return steps
            
            # 生成所有可能的下一步状态
            for i in range(4):
                # 获取当前位的数字
                digit = int(current[i])
                
                # 向上旋转（数字增加）
                up_digit = (digit + 1) % 10
                next_up = current[:i] + str(up_digit) + current[i+1:]
                # 如果新状态不在死亡集合且未被访问过
                if next_up not in dead_set and next_up not in visited:
                    visited.add(next_up)
                    queue.append((next_up, steps + 1))
                
                # 向下旋转（数字减少）
                down_digit = (digit - 1) % 10
                next_down = current[:i] + str(down_digit) + current[i+1:]
                # 如果新状态不在死亡集合且未被访问过
                if next_down not in dead_set and next_down not in visited:
                    visited.add(next_down)
                    queue.append((next_down, steps + 1))
        
        # 如果所有可能状态都遍历完仍未找到目标，返回-1
        return -1
