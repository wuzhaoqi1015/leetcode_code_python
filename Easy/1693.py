import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # 按date_id和make_name分组，计算不同的lead_id和partner_id的数量
    result = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),  # 计算不同lead_id的数量
        unique_partners=('partner_id', 'nunique')  # 计算不同partner_id的数量
    ).reset_index()  # 重置索引以将分组列转为普通列
    
    return result
