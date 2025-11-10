class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 初始化结果数组，长度为num_people，初始值都为0
        result = [0] * num_people
        # 当前要分配的糖果数量
        current_candy = 1
        # 当前分配的小朋友索引
        index = 0
        
        # 当还有糖果可分配时循环
        while candies > 0:
            # 如果剩余糖果足够分配当前轮次的糖果数
            if candies >= current_candy:
                # 给当前小朋友分配current_candy颗糖果
                result[index] += current_candy
                # 减少剩余糖果数量
                candies -= current_candy
                # 下一轮要分配的糖果数加1
                current_candy += 1
            else:
                # 如果剩余糖果不够分配当前轮次的糖果数
                # 将剩余所有糖果分配给当前小朋友
                result[index] += candies
                # 糖果分配完毕，跳出循环
                break
            
            # 移动到下一个小朋友，如果到达末尾则回到开头
            index = (index + 1) % num_people
        
        return result
