class Solution:
    def reverseVowels(self, s: str) -> str:
        # 定义元音字母集合（包含大小写）
        vowels = set('aeiouAEIOU')
        # 将字符串转换为列表便于修改
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        # 使用双指针从两端向中间遍历
        while left < right:
            # 移动左指针直到找到元音
            while left < right and s_list[left] not in vowels:
                left += 1
            # 移动右指针直到找到元音
            while left < right and s_list[right] not in vowels:
                right -= 1
            # 交换左右指针指向的元音
            s_list[left], s_list[right] = s_list[right], s_list[left]
            # 移动指针继续寻找下一对
            left += 1
            right -= 1
        
        # 将列表转换回字符串返回
        return ''.join(s_list)
