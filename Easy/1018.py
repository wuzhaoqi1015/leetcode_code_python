class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []  # 存储结果的列表
        current = 0  # 当前累积的数值，避免数值过大使用模5来保持小范围
        for num in nums:
            # 每次将当前值左移一位（相当于乘2）并加上新的二进制位
            # 使用模5来防止数值溢出并保持正确性
            current = (current * 2 + num) % 5
            # 如果模5后为0，说明当前数值能被5整除
            result.append(current == 0)
        return result
