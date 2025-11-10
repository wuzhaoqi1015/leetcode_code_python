class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []  # 初始化结果列表
        for num in nums:  # 遍历输入数组中的每个数字
            # 将数字转换为字符串，然后遍历每个字符
            for char in str(num):
                # 将字符转换回整数并添加到结果列表
                result.append(int(char))
        return result  # 返回最终结果
