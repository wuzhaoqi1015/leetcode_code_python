# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 创建员工ID到员工对象的映射字典
        employee_dict = {}
        for emp in employees:
            employee_dict[emp.id] = emp
        
        # 使用深度优先搜索计算重要度总和
        def dfs(emp_id):
            employee = employee_dict[emp_id]
            total = employee.importance
            # 递归计算所有下属的重要度
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total
        
        # 从给定ID开始计算
        return dfs(id)
