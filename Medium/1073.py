class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 反转数组以便从最低位开始处理
        arr1_rev = arr1[::-1]
        arr2_rev = arr2[::-1]
        n1, n2 = len(arr1_rev), len(arr2_rev)
        max_len = max(n1, n2) + 4  # 预留足够空间处理进位
        res = [0] * max_len
        carry = 0
        
        # 逐位相加
        for i in range(max_len):
            # 获取当前位的值，超出数组长度则为0
            a = arr1_rev[i] if i < n1 else 0
            b = arr2_rev[i] if i < n2 else 0
            total = a + b + carry
            # 在-2进制中，每位只能是0或1
            if total >= 0:
                res[i] = total % 2
                carry = -(total // 2)  # 进位规则与二进制不同
            else:
                # 处理负值情况
                res[i] = 1
                carry = 1
        
        # 去除前导零，但保留最后一个0（如果结果就是0）
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        # 反转回高位在前
        return res[::-1]
