import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 按email分组，找到每个email对应的最小id
    min_ids = person.groupby('email')['id'].min().reset_index()
    
    # 创建要删除的id列表：所有不在最小id中的id
    ids_to_keep = min_ids['id'].tolist()
    
    # 找出需要删除的行索引
    rows_to_drop = person[~person['id'].isin(ids_to_keep)].index
    
    # 直接修改原DataFrame，删除重复的行
    person.drop(rows_to_drop, inplace=True)
