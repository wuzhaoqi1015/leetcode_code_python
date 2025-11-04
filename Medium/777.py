class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # 长度必须相等
        if len(start) != len(result):
            return False
            
        n = len(start)
        i = j = 0
        
        # 双指针遍历两个字符串
        while i < n and j < n:
            # 跳过start中的'X'
            while i < n and start[i] == 'X':
                i += 1
            # 跳过result中的'X'  
            while j < n and result[j] == 'X':
                j += 1
                
            # 如果都到达末尾，返回True
            if i == n and j == n:
                return True
            # 如果一个到达末尾另一个没有，返回False
            if i == n or j == n:
                return False
                
            # 当前非X字符必须相同
            if start[i] != result[j]:
                return False
                
            # L只能向左移动，所以在start中的位置不能小于result中的位置
            if start[i] == 'L' and i < j:
                return False
            # R只能向右移动，所以在start中的位置不能大于result中的位置  
            if start[i] == 'R' and i > j:
                return False
                
            i += 1
            j += 1
            
        # 处理剩余字符
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
            
        while j < n:
            if result[j] != 'X':
                return False
            j += 1
                
        return True
