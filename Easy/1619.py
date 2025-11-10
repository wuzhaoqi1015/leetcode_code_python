class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # 首先对数组进行排序
        arr.sort()
        n = len(arr)
        # 计算需要删除的元素数量（5%）
        remove_count = n // 20
        # 删除最小5%和最大5%的元素后，取中间90%的元素
        trimmed_arr = arr[remove_count:n-remove_count]
        # 计算平均值
        return sum(trimmed_arr) / len(trimmed_arr)
