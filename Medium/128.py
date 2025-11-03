class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)  # 使用集合进行O(1)查找
        max_length = 0
        
        for num in num_set:
            # 只有当num是序列的起点时才进行处理
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # 向后查找连续的数字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # 更新最大长度
                max_length = max(max_length, current_length)
        
        return max_length
