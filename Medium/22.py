class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current, open_count, close_count):
            # 当当前字符串长度达到2*n时，说明已经完成一个有效组合
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # 如果左括号数量小于n，可以添加左括号
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # 如果右括号数量小于左括号数量，可以添加右括号
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        # 从空字符串开始回溯，初始左右括号计数都为0
        backtrack('', 0, 0)
        return result
