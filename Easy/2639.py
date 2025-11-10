class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # 获取矩阵的行数和列数
        m = len(grid)
        n = len(grid[0])
        # 初始化结果数组，长度为列数n
        ans = [0] * n
        
        # 遍历每一列
        for j in range(n):
            max_width = 0
            # 遍历当前列的每一行
            for i in range(m):
                # 将当前元素转换为字符串
                num_str = str(grid[i][j])
                # 计算当前字符串的长度
                width = len(num_str)
                # 更新当前列的最大宽度
                if width > max_width:
                    max_width = width
            # 将当前列的最大宽度存入结果数组
            ans[j] = max_width
        
        return ans
