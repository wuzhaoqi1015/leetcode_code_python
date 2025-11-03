class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 处理空字符串的特殊情况
        if not digits:
            return []
        
        # 定义数字到字母的映射关系
        phone_map = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # 使用回溯法生成所有可能的字母组合
        def backtrack(index, current_combination):
            # 如果当前组合长度等于输入数字长度，添加到结果列表
            if index == len(digits):
                result.append(current_combination)
                return
            
            # 获取当前数字对应的所有字母
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # 遍历当前数字对应的每个字母，递归生成组合
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        result = []
        backtrack(0, "")
        return result
