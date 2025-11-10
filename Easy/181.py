import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 合并员工表与经理表，使用自连接
    merged_df = employee.merge(
        employee, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )
    
    # 筛选出员工工资高于经理工资的记录
    result_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]
    
    # 选择员工姓名列并重命名为Employee
    result = result_df[['name_emp']].rename(columns={'name_emp': 'Employee'})
    
    return result
