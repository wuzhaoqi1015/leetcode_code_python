class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # 如果k是偶数或者能被5整除，则不可能有全1数能被k整除
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0  # 当前余数
        # 遍历可能的长度，从1到k
        for length in range(1, k + 1):
            # 计算当前全1数对k的余数
            # 使用模运算避免数值过大：新余数 = (旧余数 * 10 + 1) % k
            remainder = (remainder * 10 + 1) % k
            # 如果余数为0，说明找到了满足条件的长度
            if remainder == 0:
                return length
        
        # 如果遍历完1到k都没有找到，返回-1
        return -1
