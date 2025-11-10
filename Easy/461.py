class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 计算x和y的异或结果，不同位会置为1
        xor_result = x ^ y
        distance = 0
        
        # 统计异或结果中1的个数
        while xor_result:
            # 使用位运算技巧：xor_result & (xor_result - 1)会消除最低位的1
            xor_result &= xor_result - 1
            distance += 1
            
        return distance
