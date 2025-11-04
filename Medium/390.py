class Solution:
    def lastRemaining(self, n: int) -> int:
        # 初始化剩余数字数量、当前步长、起始数字和方向标志
        remaining = n
        step = 1
        start = 1
        left_to_right = True
        
        # 当剩余数字数量大于1时继续循环
        while remaining > 1:
            # 从左到右删除时，起始数字会变化
            if left_to_right:
                start += step
            # 从右到左删除时，只有当剩余数字数量为奇数时起始数字才会变化
            else:
                if remaining % 2 == 1:
                    start += step
            
            # 更新剩余数字数量（每次删除一半）
            remaining //= 2
            # 步长加倍（因为间隔删除）
            step *= 2
            # 切换方向
            left_to_right = not left_to_right
        
        # 返回最后剩下的数字
        return start
