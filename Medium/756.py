from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # 构建允许模式的映射字典，键为底部两个块，值为可能的顶部块列表
        pattern_map = defaultdict(list)
        for pattern in allowed:
            left, right, top = pattern[0], pattern[1], pattern[2]
            pattern_map[(left, right)].append(top)
        
        # 使用DFS递归构建金字塔
        def dfs(current_level):
            # 如果当前层只有一个块，说明已经到达金字塔顶部
            if len(current_level) == 1:
                return True
            
            # 为下一层生成所有可能的块组合
            next_level_candidates = []
            # 遍历当前层的相邻块对
            for i in range(len(current_level) - 1):
                left_block = current_level[i]
                right_block = current_level[i + 1]
                key = (left_block, right_block)
                
                # 如果当前块对没有对应的允许模式，直接返回False
                if key not in pattern_map:
                    return False
                
                # 如果是第一对块，初始化下一层候选
                if i == 0:
                    next_level_candidates = pattern_map[key][:]
                else:
                    # 否则，将当前块对的允许顶部块与已有候选组合进行交叉
                    new_candidates = []
                    current_tops = pattern_map[key]
                    for candidate in next_level_candidates:
                        for top in current_tops:
                            new_candidates.append(candidate + top)
                    next_level_candidates = new_candidates
            
            # 对每个可能的下一层候选进行DFS
            for candidate in next_level_candidates:
                if dfs(candidate):
                    return True
            
            return False
        
        # 从最底层开始DFS
        return dfs(bottom)
