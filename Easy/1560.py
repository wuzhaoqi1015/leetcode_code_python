class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # 初始化访问次数数组，索引0不使用，从1到n
        count = [0] * (n + 1)
        
        # 遍历所有阶段
        for i in range(len(rounds) - 1):
            start = rounds[i]
            end = rounds[i + 1]
            
            # 如果起点小于等于终点，直接遍历起点到终点（不包括终点）
            if start <= end:
                for j in range(start, end):
                    count[j] += 1
            else:
                # 起点大于终点，需要绕圈
                # 先遍历从起点到n
                for j in range(start, n + 1):
                    count[j] += 1
                # 再遍历从1到终点
                for j in range(1, end):
                    count[j] += 1
        
        # 最后一个扇区单独处理，因为每个阶段结束时会到达终点扇区
        count[rounds[-1]] += 1
        
        # 找出最大访问次数
        max_count = max(count)
        
        # 收集所有访问次数等于最大值的扇区编号
        result = []
        for i in range(1, n + 1):
            if count[i] == max_count:
                result.append(i)
                
        return result
