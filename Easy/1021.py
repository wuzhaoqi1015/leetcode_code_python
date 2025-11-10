class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []  # 存储最终结果
        balance = 0  # 记录括号平衡状态
        start = 0    # 记录原语开始位置
        
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            else:
                balance -= 1
            
            # 当balance归零时，说明找到一个完整的原语
            if balance == 0:
                # 去掉最外层括号，取原语内部内容
                result.append(s[start+1:i])
                start = i + 1  # 更新下一个原语的开始位置
        
        return ''.join(result)
