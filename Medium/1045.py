import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # 获取Product表中所有不重复的产品键
    all_products = set(product['product_key'])
    
    # 按customer_id分组，获取每个客户购买的所有不重复产品
    customer_products = customer.groupby('customer_id')['product_key'].apply(set).reset_index()
    
    # 筛选出购买了所有产品的客户
    # 检查每个客户购买的产品集合是否等于所有产品的集合
    result = customer_products[customer_products['product_key'] == all_products]
    
    # 返回只包含customer_id列的结果
    return result[['customer_id']]
