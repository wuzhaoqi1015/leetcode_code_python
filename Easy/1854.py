class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 创建年份变化数组，年份范围从1950到2050
        delta = [0] * 101  # 2050-1950+1=101
        
        # 遍历每个人的出生和死亡年份
        for birth, death in logs:
            # 出生年份对应的人口+1
            delta[birth - 1950] += 1
            # 死亡年份对应的人口-1（因为死亡年份不计入）
            delta[death - 1950] -= 1
        
        max_population = 0  # 最大人口数
        current_population = 0  # 当前人口数
        result_year = 1950  # 结果年份
        
        # 遍历所有年份，计算每年的人口数
        for year in range(101):
            current_population += delta[year]
            # 如果当前人口大于最大人口，更新最大人口和结果年份
            if current_population > max_population:
                max_population = current_population
                result_year = 1950 + year
        
        return result_year
