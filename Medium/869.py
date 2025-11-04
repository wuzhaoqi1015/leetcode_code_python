class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 将输入数字转换为字符列表并排序，得到排序后的数字特征
        sorted_n = sorted(str(n))
        
        # 遍历所有可能的2的幂次方，检查是否有与输入数字排序后相同的
        # 由于n最大为10^9，2^30约为10^9，所以遍历到2^30足够
        for i in range(31):
            # 计算2的i次幂
            power = 1 << i
            # 将2的幂转换为字符串并排序
            sorted_power = sorted(str(power))
            # 如果排序后的字符串与输入数字排序后的字符串相同，返回True
            if sorted_n == sorted_power:
                return True
        
        # 如果遍历完所有可能的2的幂都没有匹配的，返回False
        return False
