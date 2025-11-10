class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 按照每个箱子的单元数量降序排序，优先装载单元数量多的箱子
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        remaining_capacity = truckSize
        
        for boxes, units_per_box in boxTypes:
            if remaining_capacity <= 0:
                break
                
            # 计算当前类型箱子能装载的数量
            boxes_to_take = min(boxes, remaining_capacity)
            total_units += boxes_to_take * units_per_box
            remaining_capacity -= boxes_to_take
        
        return total_units
