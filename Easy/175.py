import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 使用左连接将Person表和Address表连接起来，连接键为personId
    # 这样即使Address表中没有对应的personId，Person表中的记录也会保留
    merged_df = person.merge(address, on='personId', how='left')
    
    # 选择需要的列：firstName, lastName, city, state
    result_df = merged_df[['firstName', 'lastName', 'city', 'state']]
    
    return result_df
