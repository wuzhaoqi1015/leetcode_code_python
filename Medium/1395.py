class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        # 遍历所有可能的中间位置j
        for j in range(1, n - 1):
            left_less = 0
            left_greater = 0
            right_less = 0
            right_greater = 0
            
            # 统计j左边比rating[j]小和大的元素个数
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            # 统计j右边比rating[j]小和大的元素个数
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1
            
            # 计算递增和递减的作战单位数量
            # 递增：左边比j小的数量 * 右边比j大的数量
            # 递减：左边比j大的数量 * 右边比j小的数量
            count += left_less * right_greater + left_greater * right_less
        
        return count
