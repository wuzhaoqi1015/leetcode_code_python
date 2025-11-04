class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(string):
            # 将字符串转换为字母组列表，每个组是(字符, 连续出现次数)
            groups = []
            i = 0
            n = len(string)
            while i < n:
                j = i
                while j < n and string[j] == string[i]:
                    j += 1
                groups.append((string[i], j - i))
                i = j
            return groups
        
        s_groups = get_groups(s)
        count = 0
        
        for word in words:
            word_groups = get_groups(word)
            # 如果字母组数量不同，直接跳过
            if len(word_groups) != len(s_groups):
                continue
                
            valid = True
            for i in range(len(s_groups)):
                s_char, s_count = s_groups[i]
                w_char, w_count = word_groups[i]
                
                # 字符必须相同
                if s_char != w_char:
                    valid = False
                    break
                
                # 检查扩张条件
                if s_count < w_count:
                    # 目标字符串的字符数量不能小于原单词
                    valid = False
                    break
                elif s_count > w_count and s_count < 3:
                    # 如果要扩张，目标字符串的字符数量必须至少为3
                    valid = False
                    break
            
            if valid:
                count += 1
                
        return count
