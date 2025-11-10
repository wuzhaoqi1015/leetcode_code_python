class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 初始化入度和出度数组，长度为n+1（编号从1到n）
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        # 遍历trust数组，统计每个人的入度和出度
        for a, b in trust:
            out_degree[a] += 1  # a信任别人，出度加1
            in_degree[b] += 1   # b被信任，入度加1
        
        # 遍历所有人，寻找可能的法官
        for i in range(1, n + 1):
            # 法官的条件：出度为0（不信任任何人），入度为n-1（被其他所有人信任）
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        
        # 没有找到符合条件的法官
        return -1
