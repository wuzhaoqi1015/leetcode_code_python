class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 使用集合记录已经出现过的元素
        seen = set()
        for num in nums:
            # 如果当前元素已经在集合中，说明找到了重复n次的元素
            if num in seen:
                return num
            # 将当前元素添加到集合中
            seen.add(num)
        # 理论上不会执行到这里，因为题目保证有重复元素
        return -1
