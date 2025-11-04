class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []  # 存储所有满足条件的递增子序列
        path = []    # 当前递归路径
        
        def backtrack(start_index):
            # 如果当前路径长度大于等于2，则加入结果集
            if len(path) >= 2:
                result.append(path[:])
            
            # 使用集合记录当前层已经使用过的数字，避免重复
            used = set()
            for i in range(start_index, len(nums)):
                # 如果当前数字小于路径最后一个数字，跳过（不满足递增）
                if path and nums[i] < path[-1]:
                    continue
                # 如果当前数字在当前层已经使用过，跳过（去重）
                if nums[i] in used:
                    continue
                
                used.add(nums[i])  # 记录当前层使用过的数字
                path.append(nums[i])  # 选择当前数字
                backtrack(i + 1)      # 递归到下一层
                path.pop()            # 回溯，撤销选择
        
        backtrack(0)
        return result
