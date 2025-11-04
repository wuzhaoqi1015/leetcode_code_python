import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # 定义目标日期
    target_date = '2019-08-16'
    
    # 筛选出在目标日期及之前的价格变更记录
    valid_products = products[products['change_date'] <= target_date].copy()
    
    # 按产品ID分组，找到每个产品在目标日期前的最后一次价格变更
    # 使用change_date降序排列，然后取每个组的第一个（即最近的变更）
    latest_prices = valid_products.sort_values(['product_id', 'change_date'], ascending=[True, False])
    latest_prices = latest_prices.drop_duplicates('product_id', keep='first')
    
    # 创建包含所有产品ID的DataFrame（包括那些在目标日期前没有价格变更的产品）
    all_products = pd.DataFrame({'product_id': products['product_id'].unique()})
    
    # 合并所有产品与最近价格，使用左连接
    result = all_products.merge(latest_prices[['product_id', 'new_price']], 
                               on='product_id', 
                               how='left')
    
    # 将没有价格变更记录的产品价格设置为10（初始价格）
    result['price'] = result['new_price'].fillna(10).astype(int)
    
    # 选择需要的列并重命名
    result = result[['product_id', 'price']]
    
    return result
