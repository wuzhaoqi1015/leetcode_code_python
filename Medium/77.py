class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 使用回溯法生成所有组合
        result = []
        
        def backtrack(start, current):
            # 当前组合长度等于k时，添加到结果中
            if len(current) == k:
                result.append(current[:])
                return
            
            # 遍历可能的数字
            for i in range(start, n + 1):
                current.append(i)  # 选择当前数字
                backtrack(i + 1, current)  # 递归处理下一个数字
                current.pop()  # 撤销选择
        
        backtrack(1, [])
        return result
