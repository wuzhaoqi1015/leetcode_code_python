class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        # 计算后缀和，避免重复计算
        total_shifts = [0] * n
        total_shifts[-1] = shifts[-1] % 26
        for i in range(n-2, -1, -1):
            total_shifts[i] = (total_shifts[i+1] + shifts[i]) % 26
        
        # 构建结果字符串
        result = []
        for i in range(n):
            # 计算当前字符移位后的新字符
            new_char_ord = (ord(s[i]) - ord('a') + total_shifts[i]) % 26 + ord('a')
            result.append(chr(new_char_ord))
        
        return ''.join(result)
