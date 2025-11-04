class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # 使用栈来模拟行星碰撞过程
        for ast in asteroids:
            # 当栈不为空且当前行星向左移动（负数）而栈顶行星向右移动（正数）时，可能发生碰撞
            while stack and ast < 0 < stack[-1]:
                # 比较当前行星和栈顶行星的大小
                if stack[-1] < -ast:  # 栈顶行星较小，被撞碎
                    stack.pop()
                    continue  # 继续与下一个栈顶行星比较
                elif stack[-1] == -ast:  # 大小相等，两者都爆炸
                    stack.pop()
                break  # 当前行星被撞碎或两者都爆炸，跳出循环
            else:
                # 没有发生碰撞或碰撞后当前行星存活，将当前行星入栈
                stack.append(ast)
        return stack
