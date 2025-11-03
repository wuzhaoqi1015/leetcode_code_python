class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 定义结果列表
        result = []
        # 定义回溯函数
        def backtrack(start, path, current_sum):
            # 如果当前和等于目标值，将路径加入结果
            if current_sum == target:
                result.append(path[:])
                return
            # 如果当前和超过目标值，直接返回
            if current_sum > target:
                return
            # 遍历候选数组，从start开始避免重复组合
            for i in range(start, len(candidates)):
                # 选择当前数字
                path.append(candidates[i])
                # 递归调用，注意i不变因为可以重复使用
                backtrack(i, path, current_sum + candidates[i])
                # 撤销选择
                path.pop()
        # 调用回溯函数
        backtrack(0, [], 0)
        # 返回结果
        return result
