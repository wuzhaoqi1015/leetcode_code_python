class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # 使用字典记录每个盒子的小球数量
        box_count = {}
        max_count = 0
        
        # 遍历每个小球编号
        for num in range(lowLimit, highLimit + 1):
            # 计算小球编号的数字和
            box_num = 0
            temp = num
            while temp > 0:
                box_num += temp % 10
                temp //= 10
            
            # 更新盒子中小球数量
            if box_num in box_count:
                box_count[box_num] += 1
            else:
                box_count[box_num] = 1
            
            # 更新最大数量
            if box_count[box_num] > max_count:
                max_count = box_count[box_num]
        
        return max_count
