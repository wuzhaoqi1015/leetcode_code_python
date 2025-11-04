class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for query in queries:
            # 使用双指针匹配模式
            i = 0  # 指向pattern的指针
            j = 0  # 指向query的指针
            match = True
            
            while j < len(query):
                if i < len(pattern) and query[j] == pattern[i]:
                    # 当前字符匹配成功，两个指针都前进
                    i += 1
                    j += 1
                elif query[j].islower():
                    # 当前字符是小写字母且不匹配pattern，可以跳过（视为插入的小写字母）
                    j += 1
                else:
                    # 当前字符是大写字母且不匹配pattern，匹配失败
                    match = False
                    break
            
            # 检查pattern是否完全匹配
            if i != len(pattern):
                match = False
                
            result.append(match)
        
        return result
