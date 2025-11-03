class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 对候选数组进行排序，便于后续去重处理
        candidates.sort()
        result = []
        
        def backtrack(start, path, current_sum):
            # 当前路径和等于目标值，将路径加入结果集
            if current_sum == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # 剪枝：当前数字加上已选数字和超过目标值，跳过
                if current_sum + candidates[i] > target:
                    break
                
                # 去重：跳过同一层级中相同的数字
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # 选择当前数字
                path.append(candidates[i])
                # 递归处理下一个位置，注意索引从i+1开始，避免重复使用同一元素
                backtrack(i + 1, path, current_sum + candidates[i])
                # 回溯，撤销选择
                path.pop()
        
        backtrack(0, [], 0)
        return result
