import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    # 为每个product_id找到最早出现的年份
    first_year_df = sales.groupby('product_id')['year'].min().reset_index()
    first_year_df.rename(columns={'year': 'first_year'}, inplace=True)
    
    # 将最早年份信息合并回原始销售表
    merged_df = sales.merge(first_year_df, on='product_id')
    
    # 筛选出年份等于最早年份的记录
    result_df = merged_df[merged_df['year'] == merged_df['first_year']]
    
    # 选择需要的列并返回结果
    result_df = result_df[['product_id', 'first_year', 'quantity', 'price']]
    
    return result_df
