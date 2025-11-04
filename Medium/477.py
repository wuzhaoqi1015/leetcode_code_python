class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        # 遍历32位二进制位
        for i in range(32):
            count_ones = 0
            # 统计当前位为1的数字个数
            for num in nums:
                count_ones += (num >> i) & 1
            # 当前位的汉明距离贡献 = 1的个数 * 0的个数
            total += count_ones * (n - count_ones)
        return total
