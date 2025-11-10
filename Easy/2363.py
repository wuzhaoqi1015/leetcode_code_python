from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 使用字典来存储每个价值对应的重量总和
        weight_dict = {}
        
        # 遍历items1，累加重量到对应价值
        for value, weight in items1:
            if value in weight_dict:
                weight_dict[value] += weight
            else:
                weight_dict[value] = weight
        
        # 遍历items2，累加重量到对应价值
        for value, weight in items2:
            if value in weight_dict:
                weight_dict[value] += weight
            else:
                weight_dict[value] = weight
        
        # 将字典转换为列表，并按价值升序排序
        result = [[value, weight] for value, weight in weight_dict.items()]
        result.sort(key=lambda x: x[0])
        
        return result
