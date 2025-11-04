class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # 生成格雷码序列
        gray = [i ^ (i >> 1) for i in range(1 << n)]
        # 找到start在格雷码中的位置
        idx = gray.index(start)
        # 将格雷码序列旋转，使得start作为第一个元素
        return gray[idx:] + gray[:idx]
