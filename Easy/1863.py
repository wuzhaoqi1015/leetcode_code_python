class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # 使用DFS遍历所有子集并计算异或总和
        def dfs(index, current_xor):
            # 当遍历到数组末尾时，返回当前异或值
            if index == len(nums):
                return current_xor
            # 对于每个元素，有两种选择：包含或不包含
            # 包含当前元素：更新异或值并继续递归
            include = dfs(index + 1, current_xor ^ nums[index])
            # 不包含当前元素：保持异或值不变并继续递归
            exclude = dfs(index + 1, current_xor)
            # 返回两种情况的和
            return include + exclude
        
        # 从索引0和初始异或值0开始DFS
        return dfs(0, 0)
