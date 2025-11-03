class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 使用回溯法生成全排列
        def backtrack(path, used):
            # 当前路径长度等于数组长度时，找到一个排列
            if len(path) == len(nums):
                result.append(path[:])  # 添加当前排列的副本
                return
            
            # 遍历所有可能的数字选择
            for i in range(len(nums)):
                if not used[i]:  # 如果该数字未被使用
                    used[i] = True  # 标记为已使用
                    path.append(nums[i])  # 添加到当前路径
                    backtrack(path, used)  # 递归继续构建排列
                    path.pop()  # 回溯，移除最后添加的数字
                    used[i] = False  # 标记为未使用
        
        result = []  # 存储所有排列结果
        used = [False] * len(nums)  # 记录数字使用状态
        backtrack([], used)  # 从空路径开始回溯
        return result
