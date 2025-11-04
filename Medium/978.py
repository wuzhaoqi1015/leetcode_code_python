class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        # 初始化两个状态变量，分别对应两种湍流模式
        # up表示当前元素大于前一个元素时的湍流长度
        # down表示当前元素小于前一个元素时的湍流长度
        up = 1
        down = 1
        max_len = 1
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                # 当前上升，应该在下降模式的基础上+1
                up = down + 1
                down = 1  # 重置下降模式
                max_len = max(max_len, up)
            elif arr[i] < arr[i-1]:
                # 当前下降，应该在上升模式的基础上+1
                down = up + 1
                up = 1    # 重置上升模式
                max_len = max(max_len, down)
            else:
                # 相等时重置两个状态
                up = 1
                down = 1
        
        return max_len
