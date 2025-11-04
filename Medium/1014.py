class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 初始化最大得分为0，当前最大values[i] + i为values[0] + 0
        max_score = 0
        max_i = values[0] + 0
        
        # 从第二个景点开始遍历
        for j in range(1, len(values)):
            # 计算当前景点对的最大得分
            max_score = max(max_score, max_i + values[j] - j)
            # 更新max_i为当前最大的values[i] + i
            max_i = max(max_i, values[j] + j)
        
        return max_score
