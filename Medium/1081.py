class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 记录每个字符最后出现的位置
        last_occurrence = {}
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        
        stack = []  # 单调栈，用于构建最小字典序子序列
        seen = set()  # 记录已经在栈中的字符
        
        for idx, char in enumerate(s):
            # 如果字符已经在栈中，跳过
            if char in seen:
                continue
                
            # 当栈不为空，且当前字符小于栈顶字符，且栈顶字符在后面还会出现时
            # 弹出栈顶字符，为当前字符让位
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # 将当前字符入栈
            stack.append(char)
            seen.add(char)
        
        # 将栈中字符连接成字符串返回
        return ''.join(stack)
