class Solution:
    def countAndSay(self, n: int) -> str:
        # 基本情况
        if n == 1:
            return "1"
        
        # 递归获取前一个序列
        prev = self.countAndSay(n - 1)
        result = []
        count = 1
        
        # 遍历前一个序列进行行程长度编码
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(prev[i - 1])
                count = 1
        
        # 处理最后一个字符序列
        result.append(str(count))
        result.append(prev[-1])
        
        return ''.join(result)
