class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 使用集合存储所有数字以实现O(1)查找
        num_set = set(nums)
        count = 0
        
        # 遍历数组中的每个数字作为中间元素
        for num in nums:
            # 检查是否存在前一个和后一个等差元素
            if num - diff in num_set and num + diff in num_set:
                count += 1
                
        return count
