class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = -1  # 记录当前最大1的数量
        min_index = -1  # 记录当前最大1数量对应的最小行索引
        
        # 遍历每一行
        for i in range(len(mat)):
            count = 0
            # 统计当前行中1的数量
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
            
            # 如果当前行的1数量大于已知最大值，或者数量相等但行索引更小
            if count > max_count:
                max_count = count
                min_index = i
        
        return [min_index, max_count]
