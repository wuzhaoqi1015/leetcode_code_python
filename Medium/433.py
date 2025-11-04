from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 如果目标基因不在基因库中，直接返回-1
        if endGene not in bank:
            return -1
        
        # 将基因库转换为集合，提高查找效率
        bank_set = set(bank)
        # 定义可能的基因字符
        genes = ['A', 'C', 'G', 'T']
        # 使用队列进行BFS，存储当前基因和变化次数
        queue = deque([(startGene, 0)])
        # 记录已访问的基因，避免重复处理
        visited = set()
        visited.add(startGene)
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # 如果当前基因等于目标基因，返回变化次数
            if current_gene == endGene:
                return mutations
            
            # 遍历基因的每个位置
            for i in range(8):
                # 遍历所有可能的基因字符
                for char in genes:
                    # 跳过与当前字符相同的替换
                    if char == current_gene[i]:
                        continue
                    
                    # 生成新的基因序列
                    new_gene = current_gene[:i] + char + current_gene[i+1:]
                    
                    # 检查新基因是否在基因库中且未被访问过
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))
        
        # 如果无法完成变化，返回-1
        return -1
