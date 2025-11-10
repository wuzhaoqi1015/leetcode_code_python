import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # 合并项目表和员工表，使用左连接确保所有项目数据都被保留
    merged_df = project.merge(employee, on='employee_id', how='left')
    
    # 按项目ID分组，计算每个项目的平均工作年限
    result = merged_df.groupby('project_id')['experience_years'].mean().reset_index()
    
    # 将平均工作年限四舍五入到小数点后两位
    result['average_years'] = result['experience_years'].round(2)
    
    # 选择需要的列并重命名
    result = result[['project_id', 'average_years']]
    
    return result
