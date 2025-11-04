class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n  # 记录每个位置受到的净力
        
        # 从左向右扫描，计算向右的力
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # 设置最大力
            elif dominoes[i] == 'L':
                force = 0  # 遇到L则重置力
            else:
                force = max(force - 1, 0)  # 力随时间递减
            forces[i] += force
        
        # 从右向左扫描，计算向左的力
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # 设置最大力
            elif dominoes[i] == 'R':
                force = 0  # 遇到R则重置力
            else:
                force = max(force - 1, 0)  # 力随时间递减
            forces[i] -= force
        
        # 根据净力确定最终状态
        result = []
        for f in forces:
            if f > 0:
                result.append('R')  # 净力向右
            elif f < 0:
                result.append('L')  # 净力向左
            else:
                result.append('.')  # 受力平衡
        
        return ''.join(result)
