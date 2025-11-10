class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = 0  # 记录最长工作时间
        result_id = n  # 初始化为最大可能的id值，便于后续比较最小id
        
        prev_time = 0  # 记录上一个任务的结束时间，初始为0
        
        for i in range(len(logs)):
            current_id, current_time = logs[i]
            # 计算当前任务的工作时长
            work_time = current_time - prev_time
            
            # 如果当前工作时长大于记录的最大时长
            if work_time > max_time:
                max_time = work_time
                result_id = current_id
            # 如果工作时长等于最大时长，选择id较小的
            elif work_time == max_time and current_id < result_id:
                result_id = current_id
                
            prev_time = current_time  # 更新上一个任务的结束时间
            
        return result_id
