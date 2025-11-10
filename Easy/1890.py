import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    # 筛选2020年的登录记录
    logins_2020 = logins[logins['time_stamp'].dt.year == 2020]
    
    # 按用户分组，找到每个用户的最后登录时间
    result = logins_2020.groupby('user_id')['time_stamp'].max().reset_index()
    
    # 重命名列以符合输出要求
    result = result.rename(columns={'time_stamp': 'last_stamp'})
    
    return result
