class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 使用哈希表存储每个数字的出现次数
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        count = 0
        # 遍历哈希表中的每个数字
        for num in num_count:
            # 当k为0时，需要数字出现至少两次才能形成数对
            if k == 0:
                if num_count[num] > 1:
                    count += 1
            # 当k大于0时，检查num + k是否存在于哈希表中
            else:
                if num + k in num_count:
                    count += 1
        return count
