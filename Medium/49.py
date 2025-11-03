class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用字典来存储字母异位词分组，键为排序后的字符串，值为原始字符串列表
        anagram_dict = {}
        
        # 遍历输入字符串列表
        for s in strs:
            # 将字符串排序后作为键
            sorted_str = ''.join(sorted(s))
            
            # 如果键不存在，创建新的列表
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            
            # 将原始字符串添加到对应的分组中
            anagram_dict[sorted_str].append(s)
        
        # 返回字典中所有的值（分组结果）
        return list(anagram_dict.values())
