class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # 构建树状数组
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self._update_tree(i, nums[i])
    
    def _update_tree(self, index: int, delta: int) -> None:
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    def _query_tree(self, index: int) -> int:
        res = 0
        i = index + 1
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_tree(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._query_tree(right) - self._query_tree(left - 1)
