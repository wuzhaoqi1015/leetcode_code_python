class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 使用滑动窗口方法
        left = 0  # 窗口左边界
        max_fruits = 0  # 最大水果数量
        basket = {}  # 存储当前窗口内水果种类及其数量
        
        for right in range(len(fruits)):
            # 将右边界水果加入篮子
            current_fruit = fruits[right]
            basket[current_fruit] = basket.get(current_fruit, 0) + 1
            
            # 当篮子中水果种类超过2种时，移动左边界
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            
            # 更新最大水果数量
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
