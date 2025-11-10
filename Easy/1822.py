class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 初始化负号计数器
        negative_count = 0
        
        for num in nums:
            # 如果遇到0，乘积直接为0，立即返回0
            if num == 0:
                return 0
            # 如果遇到负数，增加负号计数
            elif num < 0:
                negative_count += 1
        
        # 根据负号数量的奇偶性确定最终符号
        # 偶数个负数相乘结果为正，奇数个负数相乘结果为负
        return 1 if negative_count % 2 == 0 else -1
