from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # 将值和标签组合成元组列表
        items = list(zip(values, labels))
        # 按值降序排序
        items.sort(reverse=True, key=lambda x: x[0])
        
        # 用于记录每个标签已使用的次数
        label_count = {}
        total_sum = 0
        count = 0
        
        # 遍历排序后的项
        for value, label in items:
            # 如果已经选择了足够数量的项，提前结束
            if count >= numWanted:
                break
                
            # 检查该标签是否已达到使用限制
            if label_count.get(label, 0) < useLimit:
                total_sum += value
                count += 1
                label_count[label] = label_count.get(label, 0) + 1
                
        return total_sum
