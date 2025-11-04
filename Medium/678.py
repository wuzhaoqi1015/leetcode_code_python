class Solution:
    def checkValidString(self, s: str) -> bool:
        # 维护两个计数器，分别表示可能的最小和最大未匹配左括号数量
        min_count = 0  # 最少可能未匹配的左括号数（将*尽可能视为右括号）
        max_count = 0  # 最多可能未匹配的左括号数（将*尽可能视为左括号）
        
        for char in s:
            if char == '(':
                # 遇到左括号，最小和最大未匹配数都增加
                min_count += 1
                max_count += 1
            elif char == ')':
                # 遇到右括号，最小和最大未匹配数都减少
                min_count = max(min_count - 1, 0)  # 最小不能小于0
                max_count -= 1
                if max_count < 0:
                    # 如果最大未匹配数小于0，说明右括号太多，无法匹配
                    return False
            else:  # char == '*'
                # 遇到星号，可以视为右括号（减少min_count）、左括号（增加max_count）或空字符串
                min_count = max(min_count - 1, 0)  # 最小可能减少（视为右括号）
                max_count += 1  # 最大可能增加（视为左括号）
        
        # 最终检查最小未匹配数是否为0，表示所有左括号都能被匹配
        return min_count == 0
