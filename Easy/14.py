class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 处理空数组情况
            return ""
        
        prefix = strs[0]  # 以第一个字符串作为初始前缀
        
        for i in range(1, len(strs)):  # 遍历剩余字符串
            current_str = strs[i]
            j = 0
            # 比较当前字符串和前缀的每个字符
            while j < len(prefix) and j < len(current_str) and prefix[j] == current_str[j]:
                j += 1
            
            prefix = prefix[:j]  # 更新前缀为匹配部分
            
            if not prefix:  # 如果前缀为空，提前结束
                break
                
        return prefix
