class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将数字列表转换为字符串列表
        str_nums = [str(num) for num in nums]
        
        # 自定义比较函数：比较两个字符串拼接后的字典序
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # 使用自定义比较函数对字符串列表进行排序
        # 注意：Python 3中sorted函数不再直接支持cmp参数，需要使用functools.cmp_to_key
        import functools
        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(compare))
        
        # 将排序后的字符串连接起来
        result = ''.join(sorted_nums)
        
        # 处理特殊情况：如果结果以'0'开头（说明所有数字都是0），则返回"0"
        if result[0] == '0':
            return "0"
        
        return result
