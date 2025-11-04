class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 创建字母板坐标映射
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        char_to_pos = {}
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                char_to_pos[char] = (i, j)
        
        # 初始化当前位置和结果
        current_r, current_c = 0, 0
        result = []
        
        for char in target:
            target_r, target_c = char_to_pos[char]
            
            # 计算行和列的移动方向
            dr = target_r - current_r
            dc = target_c - current_c
            
            # 处理特殊字符'z'的情况，需要先水平移动再垂直移动
            if char == 'z':
                # 先水平移动
                if dc < 0:
                    result.append('L' * (-dc))
                elif dc > 0:
                    result.append('R' * dc)
                
                # 再垂直移动
                if dr < 0:
                    result.append('U' * (-dr))
                elif dr > 0:
                    result.append('D' * dr)
            else:
                # 对于其他字符，先垂直移动再水平移动
                if dr < 0:
                    result.append('U' * (-dr))
                elif dr > 0:
                    result.append('D' * dr)
                
                if dc < 0:
                    result.append('L' * (-dc))
                elif dc > 0:
                    result.append('R' * dc)
            
            # 添加感叹号表示选择当前字符
            result.append('!')
            
            # 更新当前位置
            current_r, current_c = target_r, target_c
        
        return ''.join(result)
