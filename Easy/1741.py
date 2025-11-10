import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # 计算每次进出所花费的时间
    employees['total_time'] = employees['out_time'] - employees['in_time']
    
    # 按员工ID和事件日期分组，计算每天的总时间
    result = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    
    # 重命名列以符合输出要求
    result = result.rename(columns={'event_day': 'day'})
    
    # 重新排列列的顺序
    result = result[['day', 'emp_id', 'total_time']]
    
    return result
