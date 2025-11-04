class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 计算所有数字的异或结果，得到两个不同数字的异或值
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # 找到异或结果中任意一个为1的位，用于区分两个不同的数字
        # 这个位表示两个数字在该位上不同
        diff_bit = xor_all & -xor_all
        
        # 根据该位将数组分成两组，分别进行异或操作
        # 这样就能分别得到两个只出现一次的数字
        num1 = 0
        num2 = 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
