import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # 合并Visits和Transactions表，使用左连接保留所有访问记录
    merged_df = visits.merge(transactions, on='visit_id', how='left')
    
    # 筛选出没有交易的访问记录（transaction_id为NaN的记录）
    no_trans_visits = merged_df[merged_df['transaction_id'].isna()]
    
    # 按customer_id分组，计算每个顾客没有交易的访问次数
    result = no_trans_visits.groupby('customer_id').size().reset_index(name='count_no_trans')
    
    return result
