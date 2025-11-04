class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        # 使用位运算优化处理大数情况
        num = n
        while num != 1:
            # 如果是偶数，直接右移一位
            if num % 2 == 0:
                num //= 2
            else:
                # 对于奇数，选择n+1或n-1中能产生更多连续0的那个
                # 特殊情况：3需要特殊处理
                if num == 3:
                    count += 2
                    break
                # 检查n+1和n-1哪个能产生更多尾随0
                if (num + 1) % 4 == 0:
                    num += 1
                else:
                    num -= 1
            count += 1
        return count
