class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}  # 用于存储状态和对应的天数
        state = tuple(cells)  # 将初始状态转换为元组以便哈希
        day = 0
        
        while day < n:
            if state in seen:
                # 检测到循环，计算剩余天数
                cycle_length = day - seen[state]
                remaining_days = (n - day) % cycle_length
                # 直接跳到最终状态
                for _ in range(remaining_days):
                    state = self.next_day(state)
                return list(state)
            
            seen[state] = day
            state = self.next_day(state)
            day += 1
        
        return list(state)
    
    def next_day(self, cells):
        # 计算下一天的状态
        next_cells = [0] * len(cells)
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                next_cells[i] = 1
            else:
                next_cells[i] = 0
        # 首尾牢房始终为0
        next_cells[0] = 0
        next_cells[-1] = 0
        return tuple(next_cells)
