class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 将字符串转换为列表便于操作
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        # 使用双指针法反转英文字母
        while left < right:
            # 找到左边第一个英文字母
            while left < right and not s_list[left].isalpha():
                left += 1
            # 找到右边第一个英文字母
            while left < right and not s_list[right].isalpha():
                right -= 1
            # 交换两个英文字母的位置
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        # 将列表转换回字符串并返回
        return ''.join(s_list)
