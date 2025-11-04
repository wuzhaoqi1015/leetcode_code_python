class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 创建一个字典来按组大小存储人员ID
        size_to_people = {}
        # 遍历所有人
        for i, size in enumerate(groupSizes):
            # 如果该组大小不在字典中，初始化一个空列表
            if size not in size_to_people:
                size_to_people[size] = []
            # 将当前人员ID添加到对应组大小的列表中
            size_to_people[size].append(i)
        
        # 初始化结果列表
        result = []
        # 遍历字典中的每个组大小和对应的人员列表
        for size, people in size_to_people.items():
            # 将人员列表按组大小分割成多个组
            for i in range(0, len(people), size):
                # 取size个人作为一个组，添加到结果中
                result.append(people[i:i+size])
        
        return result
