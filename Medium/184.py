import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 合并员工表和部门表，获取部门名称
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    
    # 按部门分组，计算每个部门的最高薪资
    max_salary_per_dept = merged_df.groupby('departmentId')['salary'].transform('max')
    
    # 筛选出薪资等于部门最高薪资的员工
    result_df = merged_df[merged_df['salary'] == max_salary_per_dept]
    
    # 选择需要的列并重命名
    result_df = result_df[['name_department', 'name_employee', 'salary']]
    result_df.columns = ['Department', 'Employee', 'Salary']
    
    return result_df
