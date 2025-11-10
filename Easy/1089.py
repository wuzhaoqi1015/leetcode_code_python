class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zero_count = arr.count(0)  # 统计数组中0的个数
        if zero_count == 0:  # 如果没有0，直接返回
            return
        
        # 从后向前遍历数组
        i = n - 1
        j = n - 1 + zero_count  # 计算扩展后的理论末尾位置
        
        while i >= 0:
            if j < n:  # 只在数组范围内写入
                arr[j] = arr[i]
            
            if arr[i] == 0:  # 遇到0需要复制
                j -= 1  # 向前移动一个位置
                if j < n:  # 只在数组范围内写入
                    arr[j] = 0
            
            i -= 1
            j -= 1
