class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4  # 超过25%的最小出现次数
        
        # 由于数组有序，超过25%的元素必然出现在arr[i], arr[i + threshold]的某个位置
        for i in range(n - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]
        
        # 理论上不会执行到这里，因为题目保证有解
        return -1
