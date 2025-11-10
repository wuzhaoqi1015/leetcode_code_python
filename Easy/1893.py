class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # 创建一个标记数组，用于记录每个整数是否被覆盖
        covered = [False] * 51  # 根据题目约束，最大值为50
        
        # 遍历所有区间，标记被覆盖的整数
        for start, end in ranges:
            for num in range(start, end + 1):
                if num <= 50:  # 确保不超出数组范围
                    covered[num] = True
        
        # 检查[left, right]范围内的每个整数是否都被覆盖
        for num in range(left, right + 1):
            if not covered[num]:
                return False
        
        return True
