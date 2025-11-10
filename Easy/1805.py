class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # 用空格替换所有非数字字符
        processed = ''.join(c if c.isdigit() else ' ' for c in word)
        # 分割字符串获取所有数字部分
        numbers = processed.split()
        # 使用集合存储去重后的整数（去除前导零）
        unique_integers = set()
        for num_str in numbers:
            # 去除前导零，如果全为零则保留一个零
            if num_str:
                # 将字符串转换为整数再转回字符串，自动去除前导零
                num_val = int(num_str)
                unique_integers.add(str(num_val))
        return len(unique_integers)
