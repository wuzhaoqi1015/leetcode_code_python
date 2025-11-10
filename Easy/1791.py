class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 星型图中中心节点会出现在所有边中
        # 检查前两条边中的公共节点即可确定中心节点
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
