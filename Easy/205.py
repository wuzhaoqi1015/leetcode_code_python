class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 创建两个字典来存储字符映射关系
        s_to_t = {}
        t_to_s = {}
        
        # 遍历字符串中的每个字符
        for char_s, char_t in zip(s, t):
            # 检查s到t的映射是否一致
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
                
            # 检查t到s的映射是否一致
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
                
        return True
