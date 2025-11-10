import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # 合并销售表和产品表，使用左连接确保保留所有销售记录
    merged_df = pd.merge(sales, product, on='product_id', how='left')
    
    # 选择需要的列：产品名称、年份和价格
    result_df = merged_df[['product_name', 'year', 'price']]
    
    # 返回结果表
    return result_df
