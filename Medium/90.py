class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 先对数组进行排序，便于后续去重
        nums.sort()
        result = []
        
        def backtrack(start, path):
            # 将当前路径加入结果集
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # 跳过重复元素，避免生成重复子集
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 选择当前元素
                path.append(nums[i])
                # 递归处理下一个位置
                backtrack(i + 1, path)
                # 回溯，撤销选择
                path.pop()
        
        backtrack(0, [])
        return result
