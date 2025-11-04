class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 将工作和利润配对并按难度排序
        jobs = sorted(zip(difficulty, profit))
        # 对工人能力进行排序
        worker.sort()
        
        total_profit = 0
        max_profit = 0
        j = 0
        
        # 遍历每个工人
        for ability in worker:
            # 找到当前工人能完成的所有工作中利润最大的
            while j < len(jobs) and ability >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            # 加上当前工人能获得的最大利润
            total_profit += max_profit
        
        return total_profit
