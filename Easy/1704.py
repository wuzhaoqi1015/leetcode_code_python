class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 定义元音字母集合（包含大小写）
        vowels = set('aeiouAEIOU')
        n = len(s)
        half = n // 2
        
        # 统计前半部分和后半部分的元音数量
        count_a = 0
        count_b = 0
        
        # 遍历前半部分
        for i in range(half):
            if s[i] in vowels:
                count_a += 1
                
        # 遍历后半部分
        for i in range(half, n):
            if s[i] in vowels:
                count_b += 1
                
        # 比较两个部分的元音数量是否相等
        return count_a == count_b
