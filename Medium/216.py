class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 初始化结果列表
        result = []
        
        # 定义回溯函数
        def backtrack(start, current_combination, current_sum):
            # 如果当前组合长度等于k且和等于n，添加到结果
            if len(current_combination) == k and current_sum == n:
                result.append(current_combination[:])
                return
            
            # 如果当前组合长度超过k或和超过n，提前返回
            if len(current_combination) > k or current_sum > n:
                return
            
            # 遍历数字1到9
            for i in range(start, 10):
                # 添加当前数字到组合
                current_combination.append(i)
                current_sum += i
                
                # 递归调用，从下一个数字开始
                backtrack(i + 1, current_combination, current_sum)
                
                # 回溯，移除当前数字
                current_combination.pop()
                current_sum -= i
        
        # 调用回溯函数
        backtrack(1, [], 0)
        
        # 返回结果
        return result
