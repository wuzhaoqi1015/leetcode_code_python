class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按身高降序、k值升序排序
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        # 根据k值作为索引插入到结果列表中
        for p in people:
            result.insert(p[1], p)
        return result
