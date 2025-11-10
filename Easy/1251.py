import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # 合并两个表，找到每个销售记录对应的价格
    merged_df = units_sold.merge(prices, on='product_id', how='left')
    
    # 筛选出购买日期在价格有效期间内的记录
    valid_sales = merged_df[
        (merged_df['purchase_date'] >= merged_df['start_date']) & 
        (merged_df['purchase_date'] <= merged_df['end_date'])
    ]
    
    # 计算每个销售记录的总价（单价 × 数量）
    valid_sales['total_price'] = valid_sales['price'] * valid_sales['units']
    
    # 按产品ID分组计算总销售额和总销售数量
    product_stats = valid_sales.groupby('product_id').agg(
        total_revenue=('total_price', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()
    
    # 计算平均价格并四舍五入到小数点后两位
    product_stats['average_price'] = (product_stats['total_revenue'] / product_stats['total_units']).round(2)
    
    # 获取所有产品的ID（包括没有销售记录的产品）
    all_products = prices['product_id'].unique()
    
    # 创建包含所有产品ID的结果DataFrame
    result = pd.DataFrame({'product_id': all_products})
    
    # 合并计算结果
    result = result.merge(product_stats[['product_id', 'average_price']], on='product_id', how='left')
    
    # 将没有销售记录的产品的平均价格设为0
    result['average_price'] = result['average_price'].fillna(0)
    
    # 返回结果，只包含产品ID和平均价格列
    return result[['product_id', 'average_price']]
