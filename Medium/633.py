class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 使用双指针方法，一个从0开始，一个从sqrt(c)开始
        left = 0
        right = int(c ** 0.5)  # 右指针最大为c的平方根取整
        
        while left <= right:
            # 计算当前两个指针的平方和
            current_sum = left * left + right * right
            
            if current_sum == c:
                return True
            elif current_sum < c:
                # 如果平方和小于c，左指针右移
                left += 1
            else:
                # 如果平方和大于c，右指针左移
                right -= 1
        
        # 遍历完所有可能后没有找到符合条件的数对
        return False
