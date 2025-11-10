class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')  # 初始化最小距离为无穷大
        for i in range(len(nums)):
            if nums[i] == target:  # 找到目标值
                distance = abs(i - start)  # 计算当前距离
                if distance < min_distance:  # 更新最小距离
                    min_distance = distance
        return min_distance  # 返回最小距离
