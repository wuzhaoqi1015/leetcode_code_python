class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # 遍历从1到n的所有整数
        for i in range(1, n + 1):
            # 将整数转换为二进制字符串，并去掉'0b'前缀
            bin_str = bin(i)[2:]
            # 检查二进制字符串是否是s的子串
            if bin_str not in s:
                return False
        return True
