class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数不是回文数
        if x < 0:
            return False
        
        # 个位数为0且不是0的数不是回文数
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        original = x
        
        # 反转数字的后半部分
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # 比较前半部分和反转后的后半部分
        # 对于偶数位数：x == reversed_half
        # 对于奇数位数：x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
