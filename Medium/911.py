from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []  # 存储每个时间点的领先候选人
        votes = {}  # 记录每个候选人的得票数
        current_leader = -1
        max_votes = 0
        
        for i in range(len(persons)):
            person = persons[i]
            # 更新候选人得票数
            votes[person] = votes.get(person, 0) + 1
            
            # 检查是否需要更新领先者
            if votes[person] >= max_votes:
                max_votes = votes[person]
                current_leader = person
            
            # 记录当前时间点的领先者
            self.leaders.append(current_leader)

    def q(self, t: int) -> int:
        # 使用二分查找找到小于等于t的最大时间点
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1
        # right指向小于等于t的最后一个时间点
        return self.leaders[right]
