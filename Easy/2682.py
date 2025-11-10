class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # 初始化访问数组，记录每个朋友接到球的次数
        visited = [0] * n
        # 当前持球的朋友编号（从0开始计算，对应题目中的1~n）
        current = 0
        # 当前轮次
        round_num = 1
        
        # 模拟传球过程，直到有人第二次接到球
        while True:
            # 当前朋友接到球，计数加1
            visited[current] += 1
            # 如果当前朋友第二次接到球，游戏结束
            if visited[current] == 2:
                break
            # 计算下一轮持球朋友的位置：(当前位置 + 轮次 * k) % n
            current = (current + round_num * k) % n
            # 轮次增加
            round_num += 1
        
        # 收集所有从未接到过球的朋友（访问次数为0）
        losers = []
        for i in range(n):
            if visited[i] == 0:
                losers.append(i + 1)  # 转换为1-based编号
                
        return losers
