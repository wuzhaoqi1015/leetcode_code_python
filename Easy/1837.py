class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # 初始化总和为0
        total = 0
        # 当n大于0时循环处理
        while n > 0:
            # 计算当前位的余数并加到总和
            total += n % k
            # 更新n为除以k的整数部分
            n //= k
        # 返回各位数字的总和
        return total
