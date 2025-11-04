class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 对体重数组进行排序
        people.sort()
        # 初始化双指针
        left, right = 0, len(people) - 1
        boats = 0
        
        # 使用双指针遍历数组
        while left <= right:
            # 如果最轻和最重的人可以同乘一艘船
            if people[left] + people[right] <= limit:
                left += 1  # 最轻的人上船
                right -= 1  # 最重的人上船
            else:
                # 如果太重，只能最重的人单独一艘船
                right -= 1
            boats += 1  # 使用一艘船
            
        return boats
