class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # 使用集合来存储所有可能的按位或结果
        result = set()
        current = set()
        # 遍历数组中的每个元素
        for num in arr:
            # 创建新的临时集合存储当前步骤的按位或结果
            temp = {num}
            # 对当前已有的每个按位或结果进行更新
            for val in current:
                temp.add(val | num)
            # 更新当前集合为临时集合
            current = temp
            # 将当前集合中的所有结果加入最终结果集
            result |= current
        # 返回结果集的大小
        return len(result)
