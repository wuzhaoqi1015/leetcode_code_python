class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 记录每个字符最后出现的位置
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        stack = []  # 单调栈
        seen = set()  # 记录栈中已存在的字符
        
        for i, char in enumerate(s):
            # 如果字符已经在栈中，跳过
            if char in seen:
                continue
                
            # 维护单调栈：当栈不为空，且当前字符小于栈顶字符，且栈顶字符在后面还会出现
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                # 弹出栈顶字符，并从seen中移除
                removed = stack.pop()
                seen.remove(removed)
            
            # 将当前字符入栈
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
