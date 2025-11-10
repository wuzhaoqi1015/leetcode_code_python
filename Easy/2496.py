class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0  # 初始化最大值
        for s in strs:  # 遍历字符串数组
            if s.isdigit():  # 如果字符串只包含数字
                # 转换为整数（自动处理前导零）
                num = int(s)
                # 更新最大值
                if num > max_val:
                    max_val = num
            else:  # 字符串包含字母
                # 计算字符串长度
                length = len(s)
                # 更新最大值
                if length > max_val:
                    max_val = length
        return max_val  # 返回最大值
