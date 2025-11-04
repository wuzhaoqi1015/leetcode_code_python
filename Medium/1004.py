class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # 如果当前元素是0，增加zero_count
            if nums[right] == 0:
                zero_count += 1
            
            # 当窗口内0的数量超过k时，移动左指针
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length
