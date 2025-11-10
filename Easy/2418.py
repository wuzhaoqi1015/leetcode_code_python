class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 创建包含姓名和身高的元组列表
        people = list(zip(names, heights))
        # 根据身高降序排序
        people.sort(key=lambda x: x[1], reverse=True)
        # 提取排序后的姓名列表
        result = [person[0] for person in people]
        return result
