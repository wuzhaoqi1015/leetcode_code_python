class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # 创建三个字典用于不同规则的匹配
        exact_match = set(wordlist)  # 精确匹配（区分大小写）
        case_insensitive = {}  # 不区分大小写的匹配
        vowel_insensitive = {}  # 忽略元音大小写的匹配
        
        # 预处理wordlist，填充字典
        for word in wordlist:
            # 不区分大小写的匹配
            lower_word = word.lower()
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            
            # 忽略元音大小写的匹配
            vowel_key = self.get_vowel_key(word)
            if vowel_key not in vowel_insensitive:
                vowel_insensitive[vowel_key] = word
        
        result = []
        for query in queries:
            # 规则1：精确匹配
            if query in exact_match:
                result.append(query)
                continue
            
            # 规则2：不区分大小写匹配
            lower_query = query.lower()
            if lower_query in case_insensitive:
                result.append(case_insensitive[lower_query])
                continue
            
            # 规则3：忽略元音大小写匹配
            vowel_key = self.get_vowel_key(query)
            if vowel_key in vowel_insensitive:
                result.append(vowel_insensitive[vowel_key])
                continue
            
            # 无匹配项
            result.append("")
        
        return result
    
    def get_vowel_key(self, word: str) -> str:
        # 将单词转换为小写，并将所有元音替换为'*'
        vowels = set('aeiou')
        key_chars = []
        for char in word.lower():
            if char in vowels:
                key_chars.append('*')
            else:
                key_chars.append(char)
        return ''.join(key_chars)
