class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        # 创建前缀异或数组，prefix[0] = 0，prefix[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        # 初始化结果列表
        res = []
        # 处理每个查询
        for query in queries:
            left, right = query
            # 利用前缀异或性质：arr[left] ^ ... ^ arr[right] = prefix[right+1] ^ prefix[left]
            res.append(prefix[right + 1] ^ prefix[left])
        
        return res
