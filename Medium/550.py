import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # 按player_id分组，找到每个玩家的首次登录日期
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.rename(columns={'event_date': 'first_date'}, inplace=True)
    
    # 合并原始表与首次登录日期，标记首次登录的第二天日期
    merged_df = activity.merge(first_login, on='player_id')
    merged_df['next_day'] = merged_df['first_date'] + pd.Timedelta(days=1)
    
    # 筛选出在首次登录第二天有登录记录的玩家
    second_day_players = merged_df[merged_df['event_date'] == merged_df['next_day']]['player_id'].unique()
    
    # 计算总玩家数
    total_players = activity['player_id'].nunique()
    
    # 计算第二天登录的玩家数
    second_day_count = len(second_day_players)
    
    # 计算比率并四舍五入到小数点后两位
    fraction = round(second_day_count / total_players, 2) if total_players > 0 else 0.0
    
    # 创建结果DataFrame
    result = pd.DataFrame({'fraction': [fraction]})
    
    return result
