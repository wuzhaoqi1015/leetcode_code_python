class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 初始化最大重复值
        max_k = 0
        # 构建重复字符串，从1次开始尝试
        repeated = word
        # 当重复字符串长度不超过sequence长度时循环
        while len(repeated) <= len(sequence):
            # 检查当前重复字符串是否是sequence的子串
            if repeated in sequence:
                max_k += 1
                # 继续增加重复次数
                repeated += word
            else:
                # 如果不是子串，立即退出循环
                break
        return max_k
