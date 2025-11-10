class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # 使用字典统计偶数元素的频率
        freq = {}
        for num in nums:
            if num % 2 == 0:  # 只处理偶数
                freq[num] = freq.get(num, 0) + 1
        
        # 如果没有偶数元素，返回-1
        if not freq:
            return -1
        
        # 找出出现频率最高的偶数，频率相同时取最小值
        max_freq = 0
        result = float('inf')
        for num, count in freq.items():
            if count > max_freq:
                max_freq = count
                result = num
            elif count == max_freq and num < result:
                result = num
        
        return result
