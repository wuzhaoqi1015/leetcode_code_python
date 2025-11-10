class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0  # 记录当前L和R的差值
        result = 0  # 记录平衡子串的数量
        
        for char in s:
            # 遇到L则计数加1，遇到R则计数减1
            if char == 'L':
                count += 1
            else:
                count -= 1
            
            # 当计数为0时，说明遇到了一个平衡子串
            if count == 0:
                result += 1
                
        return result
