class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_needed = 0  # 需要添加的左括号数量
        right_needed = 0  # 需要添加的右括号数量
        
        for char in s:
            if char == '(':
                # 遇到左括号，需要匹配的右括号数量加1
                right_needed += 1
            else:
                # 遇到右括号
                if right_needed > 0:
                    # 如果有需要匹配的右括号，消耗一个
                    right_needed -= 1
                else:
                    # 如果没有需要匹配的右括号，需要添加一个左括号
                    left_needed += 1
        
        # 总添加数量 = 需要添加的左括号 + 剩余的右括号需求
        return left_needed + right_needed
