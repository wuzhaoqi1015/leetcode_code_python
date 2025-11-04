class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                # 如果最后两个字符相同，需要添加另一种字符
                if res[-1] == 'a':
                    res.append('b')
                    b -= 1
                else:
                    res.append('a')
                    a -= 1
            else:
                # 优先添加剩余数量较多的字符
                if a > b:
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
        return ''.join(res)
