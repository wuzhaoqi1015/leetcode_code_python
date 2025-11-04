class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 计算left和right的公共前缀
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # 将公共前缀左移shift位得到结果
        return left << shift
