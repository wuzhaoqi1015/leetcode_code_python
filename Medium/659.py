class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import Counter, defaultdict
        freq = Counter(nums)  # 统计每个数字出现的频率
        need = defaultdict(int)  # 记录需要某个数字来延长已有子序列的次数
        
        for num in nums:
            if freq[num] == 0:  # 当前数字已经被使用完
                continue
                
            if need[num] > 0:  # 当前数字可以接在某个已有子序列的后面
                freq[num] -= 1
                need[num] -= 1
                need[num + 1] += 1  # 需要下一个数字来继续延长这个子序列
            elif freq[num] > 0 and freq.get(num + 1, 0) > 0 and freq.get(num + 2, 0) > 0:  # 可以组成新的长度为3的子序列
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1  # 需要num+3来延长这个新子序列
            else:  # 无法组成满足条件的子序列
                return False
                
        return True
