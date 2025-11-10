class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # 将allowed字符串转换为集合，便于快速查找
        allowed_set = set(allowed)
        count = 0
        
        # 遍历words中的每个字符串
        for word in words:
            # 检查当前字符串的所有字符是否都在allowed_set中
            consistent = True
            for char in word:
                if char not in allowed_set:
                    consistent = False
                    break
            
            # 如果所有字符都在allowed_set中，则计数加1
            if consistent:
                count += 1
        
        return count
