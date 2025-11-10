class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 处理特殊情况：n小于等于0时直接返回False
        if n <= 0:
            return False
        
        # 使用对数方法判断是否为3的幂
        # 计算log3(n)，检查是否为整数
        import math
        # 由于浮点数精度问题，使用round取整后验证
        log_result = math.log(n, 3)
        # 将结果四舍五入到最接近的整数
        rounded_log = round(log_result)
        
        # 检查3的rounded_log次方是否等于n
        return 3 ** rounded_log == n
