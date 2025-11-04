class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 初始化偶数和
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer = []
        
        # 遍历每个查询
        for val, idx in queries:
            # 保存修改前的值
            old_val = nums[idx]
            
            # 如果旧值是偶数，从偶数和减去
            if old_val % 2 == 0:
                even_sum -= old_val
            
            # 更新数组中的值
            nums[idx] += val
            
            # 如果新值是偶数，加到偶数和上
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            
            # 将当前偶数和加入结果
            answer.append(even_sum)
        
        return answer
