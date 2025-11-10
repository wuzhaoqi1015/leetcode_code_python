class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0  # 初始化计数器
        for num in nums:  # 遍历数组中的每个数字
            # 将数字转换为字符串并计算长度，判断长度是否为偶数
            if len(str(num)) % 2 == 0:
                count += 1  # 满足条件则计数加1
        return count  # 返回最终计数结果
