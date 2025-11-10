class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            # 检查数字是否为偶数且能被3整除
            if num % 2 == 0 and num % 3 == 0:
                total += num
                count += 1
        # 如果没有符合条件的数字，返回0
        if count == 0:
            return 0
        # 计算平均值并向下取整
        return total // count
