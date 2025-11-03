class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 处理特殊情况：如果任一数字为"0"，乘积直接为"0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # 获取两个数字字符串的长度
        m, n = len(num1), len(num2)
        # 初始化结果数组，长度为m+n（最大可能位数）
        res = [0] * (m + n)
        
        # 从低位到高位遍历num1
        for i in range(m - 1, -1, -1):
            # 从低位到高位遍历num2
            for j in range(n - 1, -1, -1):
                # 计算当前位的乘积
                mul = int(num1[i]) * int(num2[j])
                # 乘积在结果数组中的位置
                p1, p2 = i + j, i + j + 1
                # 当前乘积加上低位已有的进位值
                total = mul + res[p2]
                # 计算进位和当前位值
                res[p2] = total % 10
                res[p1] += total // 10
        
        # 将结果数组转换为字符串，跳过前导零
        result_str = ""
        for num in res:
            # 如果结果字符串不为空或者当前数字不为0，则添加
            if result_str or num != 0:
                result_str += str(num)
        
        # 如果结果字符串为空，说明结果是0，否则返回结果字符串
        return result_str if result_str else "0"
