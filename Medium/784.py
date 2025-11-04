class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # 使用BFS方法生成所有可能的字符串
        from collections import deque
        
        queue = deque()
        queue.append("")  # 初始化队列，从空字符串开始
        
        # 遍历输入字符串的每个字符
        for char in s:
            level_size = len(queue)
            
            # 处理当前层的所有字符串
            for _ in range(level_size):
                current = queue.popleft()
                
                # 如果当前字符是数字，直接添加到所有现有字符串后面
                if char.isdigit():
                    queue.append(current + char)
                else:
                    # 如果是字母，分别添加小写和大写版本
                    queue.append(current + char.lower())
                    queue.append(current + char.upper())
        
        # 将队列转换为列表返回
        return list(queue)
