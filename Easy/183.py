import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 使用左连接将customers表与orders表连接，连接键为customers的id和orders的customerId
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    
    # 筛选出在orders表中没有对应记录的客户（即customerId为NaN的行）
    no_orders_customers = merged_df[merged_df['customerId'].isna()]
    
    # 选择需要的列，只保留客户姓名，并重命名列名为'Customers'
    result = no_orders_customers[['name']].rename(columns={'name': 'Customers'})
    
    return result
