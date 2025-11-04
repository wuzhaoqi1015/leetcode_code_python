class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 初始化金字塔的流量数组，最多100层
        flow = [[0.0] * (i + 1) for i in range(query_row + 2)]
        flow[0][0] = poured  # 顶层倒入所有香槟
        
        # 模拟香槟流动过程
        for i in range(query_row + 1):
            for j in range(i + 1):
                if flow[i][j] > 1.0:  # 当前杯子溢出
                    overflow = flow[i][j] - 1.0
                    flow[i][j] = 1.0  # 当前杯子满杯
                    # 溢出部分平均分到下一层的两个杯子
                    flow[i + 1][j] += overflow / 2.0
                    flow[i + 1][j + 1] += overflow / 2.0
        
        # 返回查询杯子的香槟比例，最大为1.0
        return min(1.0, flow[query_row][query_glass])
