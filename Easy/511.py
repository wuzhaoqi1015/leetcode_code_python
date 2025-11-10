import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # 按player_id分组，找到每个玩家的最早event_date作为first_login
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    # 重命名列以符合输出要求
    result = result.rename(columns={'event_date': 'first_login'})
    return result
