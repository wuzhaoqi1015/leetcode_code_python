import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # 过滤出2019-07-27及之前30天内的数据
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days=29)
    
    # 筛选在时间范围内的记录
    filtered_activity = activity[
        (pd.to_datetime(activity['activity_date']) >= start_date) & 
        (pd.to_datetime(activity['activity_date']) <= end_date)
    ]
    
    # 按日期和用户去重，统计每日活跃用户数
    daily_active = filtered_activity.groupby('activity_date')['user_id'].nunique().reset_index()
    
    # 重命名列
    daily_active.columns = ['day', 'active_users']
    
    # 按日期排序（虽然题目说任意顺序，但通常按日期排序更合理）
    daily_active = daily_active.sort_values('day')
    
    return daily_active
