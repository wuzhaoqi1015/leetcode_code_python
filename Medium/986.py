class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 初始化两个指针和结果列表
        i, j = 0, 0
        result = []
        
        # 遍历两个区间列表
        while i < len(firstList) and j < len(secondList):
            # 获取当前两个区间
            first_interval = firstList[i]
            second_interval = secondList[j]
            
            # 计算两个区间的交集
            start = max(first_interval[0], second_interval[0])
            end = min(first_interval[1], second_interval[1])
            
            # 如果存在有效交集，则添加到结果中
            if start <= end:
                result.append([start, end])
            
            # 移动指针：结束值较小的区间指针前进
            if first_interval[1] < second_interval[1]:
                i += 1
            else:
                j += 1
        
        return result
