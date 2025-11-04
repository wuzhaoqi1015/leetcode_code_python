class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 初始化结果列表，从1开始
        result = list(range(1, n + 1))
        
        # 当k大于1时，需要调整部分元素的位置来产生k个不同的差值
        # 策略：将前k+1个元素重新排列，形成k个不同的差值
        # 排列模式：1, k+1, 2, k, 3, k-1, ...
        left = 1
        right = k + 1
        index = 0
        
        # 重新排列前k+1个元素
        while left <= right:
            if left == right:
                result[index] = left
                index += 1
            else:
                result[index] = left
                result[index + 1] = right
                index += 2
            left += 1
            right -= 1
        
        # 剩余元素保持原有顺序
        # 从k+2到n的元素已经在正确位置，无需调整
        return result
