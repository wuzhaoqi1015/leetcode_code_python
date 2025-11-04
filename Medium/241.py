class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 使用字典缓存子问题的结果，避免重复计算
        memo = {}
        
        def compute(left, right):
            # 如果当前子串已经在缓存中，直接返回结果
            if (left, right) in memo:
                return memo[(left, right)]
            
            # 存储当前子串的所有可能计算结果
            res = []
            
            # 遍历整个子串，寻找运算符
            for i in range(left, right):
                char = expression[i]
                # 如果当前字符是运算符
                if char in ['+', '-', '*']:
                    # 递归计算运算符左边的所有可能结果
                    left_results = compute(left, i)
                    # 递归计算运算符右边的所有可能结果
                    right_results = compute(i + 1, right)
                    
                    # 将左右两边结果进行组合计算
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            # 如果res为空，说明当前子串没有运算符，是一个纯数字
            if not res:
                res.append(int(expression[left:right]))
            
            # 将结果存入缓存
            memo[(left, right)] = res
            return res
        
        # 从整个字符串开始计算
        return compute(0, len(expression))
