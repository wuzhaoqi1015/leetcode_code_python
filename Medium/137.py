class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用位运算统计每一位出现的次数
        # 对于出现三次的数字，每一位的1出现次数应该是3的倍数
        result = 0
        for i in range(32):
            count = 0
            # 统计第i位为1的数字个数
            for num in nums:
                # 通过右移和与操作检查第i位是否为1
                if (num >> i) & 1:
                    count += 1
            # 如果该位1的个数不是3的倍数，说明只出现一次的数字在该位为1
            if count % 3 == 1:
                # 对于负数，需要特殊处理最高位
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        return result
