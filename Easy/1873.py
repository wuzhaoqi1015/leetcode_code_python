import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # 创建奖金列的副本，初始化为0
    employees['bonus'] = 0
    
    # 筛选符合条件的雇员：id为奇数且名字不以'M'开头
    condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    
    # 对符合条件的雇员设置奖金为工资的100%
    employees.loc[condition, 'bonus'] = employees.loc[condition, 'salary']
    
    # 选择需要的列并按照employee_id排序
    result = employees[['employee_id', 'bonus']].sort_values('employee_id')
    
    return result
