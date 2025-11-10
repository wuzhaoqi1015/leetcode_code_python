import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # 计算总用户数
    total_users = len(users)
    
    # 统计每个赛事的注册用户数
    contest_counts = register.groupby('contest_id')['user_id'].nunique().reset_index()
    contest_counts.columns = ['contest_id', 'registered_count']
    
    # 计算注册百分比，保留两位小数
    contest_counts['percentage'] = round((contest_counts['registered_count'] / total_users) * 100, 2)
    
    # 按百分比降序、contest_id升序排序
    result = contest_counts.sort_values(['percentage', 'contest_id'], ascending=[False, True])
    
    # 选择需要的列并返回结果
    return result[['contest_id', 'percentage']]
