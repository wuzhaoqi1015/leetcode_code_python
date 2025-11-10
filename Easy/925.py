class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0  # 双指针分别指向name和typed的当前位置
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1  # 处理长按情况
            else:
                return False
        return i == len(name)  # 检查name是否全部匹配完成
