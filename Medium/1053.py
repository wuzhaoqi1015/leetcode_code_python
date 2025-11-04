class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # 从右向左找到第一个满足arr[i] > arr[i+1]的位置
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        # 如果整个数组都是非递减的，说明已经是最小排列，直接返回
        if i < 0:
            return arr
        # 从右向左找到第一个小于arr[i]的最大值的位置
        j = n - 1
        while j > i and arr[j] >= arr[i]:
            j -= 1
        # 如果有多个相同的值，选择最左边的那个
        while j > i and arr[j] == arr[j-1]:
            j -= 1
        # 交换arr[i]和arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        return arr
