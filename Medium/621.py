from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 统计每个任务出现的次数
        task_counts = Counter(tasks)
        # 获取出现次数最多的任务的出现次数
        max_count = max(task_counts.values())
        # 统计出现次数等于最大次数的任务有多少个
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # 计算最短时间间隔
        # 公式：(max_count - 1) * (n + 1) + max_count_tasks
        # 解释：
        # - (max_count - 1) 表示需要安排多少个完整周期
        # - (n + 1) 表示每个周期的长度（任务 + 冷却时间）
        # - max_count_tasks 表示最后一个周期需要执行的任务数量
        result = (max_count - 1) * (n + 1) + max_count_tasks
        
        # 如果计算出的结果小于任务总数，说明不需要额外的空闲时间
        # 直接返回任务总数即可
        return max(result, len(tasks))
