import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # 首先筛选出所有primary_flag为'Y'的记录
    primary_departments = employee[employee['primary_flag'] == 'Y']
    
    # 找出只有一个部门的员工
    department_count = employee.groupby('employee_id').size().reset_index(name='count')
    single_department_employees = department_count[department_count['count'] == 1]
    
    # 获取只有一个部门的员工的记录
    single_department_records = employee.merge(
        single_department_employees[['employee_id']], 
        on='employee_id', 
        how='inner'
    )
    
    # 合并两种情况：有明确primary_flag='Y'的记录和只有一个部门的记录
    result = pd.concat([primary_departments, single_department_records], ignore_index=True)
    
    # 去重，因为有些只有一个部门的员工可能在primary_departments中已经存在
    result = result.drop_duplicates(subset=['employee_id', 'department_id'])
    
    # 只保留需要的列
    result = result[['employee_id', 'department_id']]
    
    return result
