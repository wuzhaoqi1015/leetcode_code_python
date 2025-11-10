import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # 筛选同时满足低脂和可回收条件的产品
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # 选择并返回产品ID列
    result = filtered_products[['product_id']]
    
    return result
