class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        s_list = list(s)  # 转换为列表便于修改
        
        for i in range(n):
            if s_list[i] == '?':
                # 检查左右相邻字符，避免连续重复
                for char in 'abc':  # 只需要三个字母就能保证找到不重复的
                    # 检查左边字符
                    if i > 0 and s_list[i-1] == char:
                        continue
                    # 检查右边字符
                    if i < n-1 and s_list[i+1] == char:
                        continue
                    s_list[i] = char
                    break
        
        return ''.join(s_list)
