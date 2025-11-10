import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # 按user_id分组，计算每个用户的关注者数量
    result = followers.groupby('user_id')['follower_id'].count().reset_index()
    # 重命名列名为题目要求的格式
    result.columns = ['user_id', 'followers_count']
    # 按user_id升序排序
    result = result.sort_values('user_id')
    # 重置索引并丢弃原索引列
    result = result.reset_index(drop=True)
    return result
