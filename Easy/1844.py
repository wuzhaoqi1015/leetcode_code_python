class Solution:
    def replaceDigits(self, s: str) -> str:
        # 将字符串转换为列表便于修改
        s_list = list(s)
        # 遍历奇数下标位置
        for i in range(1, len(s), 2):
            # 获取前一个字符和当前数字
            prev_char = s_list[i-1]
            digit = int(s_list[i])
            # 计算移位后的字符
            shifted_char = chr(ord(prev_char) + digit)
            # 替换数字为移位后的字符
            s_list[i] = shifted_char
        # 将列表转换回字符串
        return ''.join(s_list)
