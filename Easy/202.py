class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # 用于记录已经出现过的数字，检测循环
        while n != 1:
            if n in seen:  # 如果数字已经出现过，说明进入循环，不是快乐数
                return False
            seen.add(n)  # 将当前数字加入集合
            total = 0
            # 计算数字各位的平方和
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            n = total  # 更新n为平方和
        return True  # 当n变为1时，是快乐数
