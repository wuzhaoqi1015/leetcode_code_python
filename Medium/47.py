class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 先对数组进行排序，便于后续去重
        nums.sort()
        result = []
        used = [False] * len(nums)  # 标记数组，记录元素是否被使用过
        
        def backtrack(path):
            # 当路径长度等于原数组长度时，找到一个排列
            if len(path) == len(nums):
                result.append(path[:])  # 添加当前路径的副本到结果中
                return
            
            for i in range(len(nums)):
                # 如果当前元素已被使用，跳过
                if used[i]:
                    continue
                # 去重条件：当前元素与前一个元素相同，且前一个元素未被使用
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # 选择当前元素
                used[i] = True
                path.append(nums[i])
                
                # 递归探索
                backtrack(path)
                
                # 撤销选择
                path.pop()
                used[i] = False
        
        backtrack([])
        return result
