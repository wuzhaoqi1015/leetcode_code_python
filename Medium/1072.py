class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict
        
        pattern_count = defaultdict(int)
        
        for row in matrix:
            # 如果第一个元素是1，翻转整行，使得所有行都以0开头
            if row[0] == 1:
                pattern = tuple(1 - x for x in row)
            else:
                pattern = tuple(row)
            
            pattern_count[pattern] += 1
        
        # 返回出现次数最多的模式数量
        return max(pattern_count.values())
