class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        result = []
        # 遍历字符串中的每个字符
        for char in s:
            if char == 'I':
                # 遇到'I'时，将当前最小值加入结果，最小值加1
                result.append(low)
                low += 1
            else:
                # 遇到'D'时，将当前最大值加入结果，最大值减1
                result.append(high)
                high -= 1
        # 最后将剩余的一个数字加入结果
        result.append(low)
        return result
