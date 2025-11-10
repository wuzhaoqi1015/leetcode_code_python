import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # 按actor_id和director_id分组，计算每个组合的出现次数
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
    # 筛选出合作次数大于等于3次的组合
    result = grouped[grouped['count'] >= 3]
    
    # 只返回actor_id和director_id列
    return result[['actor_id', 'director_id']]
