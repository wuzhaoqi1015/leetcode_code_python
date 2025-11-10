class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 创建期望高度数组，即排序后的heights
        expected = sorted(heights)
        count = 0
        # 遍历比较每个位置的高度是否匹配
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
