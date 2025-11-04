class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []  # 使用栈来存储当前层的分数
        score = 0   # 当前层的累计分数
        
        for char in s:
            if char == '(':
                # 遇到左括号，将当前分数压入栈并重置
                stack.append(score)
                score = 0
            else:
                # 遇到右括号，弹出栈顶的分数
                prev_score = stack.pop()
                # 如果当前分数为0，说明是一对空括号，得1分
                # 否则当前层分数需要乘以2
                if score == 0:
                    score = prev_score + 1
                else:
                    score = prev_score + 2 * score
        
        return score
