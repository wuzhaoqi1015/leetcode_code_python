class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 使用计数排序，因为年龄范围在1到120之间
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        # 计算前缀和，用于快速计算年龄区间内的用户数量
        prefix_sum = [0] * 121
        for i in range(1, 121):
            prefix_sum[i] = prefix_sum[i-1] + count[i]
        
        result = 0
        # 遍历所有可能的年龄
        for age_x in range(1, 121):
            if count[age_x] == 0:
                continue
                
            # 计算满足条件的年龄y的最小值
            min_age_y = int(0.5 * age_x + 7) + 1
            # 如果min_age_y大于age_x，说明没有满足条件的y
            if min_age_y > age_x:
                continue
                
            # 计算满足条件的年龄y的最大值
            max_age_y = age_x
            
            # 根据条件3调整：如果age_x < 100，那么age_y不能>100
            if age_x < 100:
                max_age_y = min(max_age_y, 100)
            
            # 确保min_age_y不超过max_age_y
            if min_age_y > max_age_y:
                continue
            
            # 计算年龄在[min_age_y, max_age_y]范围内的用户数量
            num_y = prefix_sum[max_age_y] - prefix_sum[min_age_y - 1]
            
            # 如果x和y年龄相同，需要减去自己
            if min_age_y <= age_x <= max_age_y:
                num_y -= 1
            
            # 每个年龄为x的用户可以向num_y个用户发送请求
            result += count[age_x] * num_y
        
        return result
