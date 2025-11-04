class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        # 创建前缀异或数组，每个位置记录字符出现次数的奇偶性
        prefix = [0] * (n + 1)
        for i in range(n):
            # 用位运算记录字符出现次数的奇偶性
            prefix[i+1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))
        
        result = []
        for left, right, k in queries:
            # 计算子串中字符出现次数的奇偶性
            xor_val = prefix[right+1] ^ prefix[left]
            # 统计出现奇数次的字符数量
            odd_count = bin(xor_val).count('1')
            # 需要替换的字符数量至少为 odd_count // 2
            # 因为可以通过重新排列和替换来消除奇数次的字符
            result.append(odd_count // 2 <= k)
        
        return result
