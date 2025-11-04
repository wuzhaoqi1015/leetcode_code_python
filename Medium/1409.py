class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # 初始化排列P
        P = list(range(1, m + 1))
        # 存储结果的列表
        result = []
        
        # 遍历每个查询
        for query in queries:
            # 查找当前查询值在P中的位置
            pos = P.index(query)
            # 将位置添加到结果中
            result.append(pos)
            # 将查询值移动到排列的开头
            P.pop(pos)
            P.insert(0, query)
        
        return result
