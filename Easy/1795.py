import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # 使用melt函数将宽表转换为长表
    # id_vars指定保持不变的列，这里是product_id
    # value_vars指定要转换的列，这里是store1, store2, store3
    # var_name指定新列名，用于存储商店名称
    # value_name指定新列名，用于存储价格
    melted_df = products.melt(
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )
    
    # 删除价格为null的行，即该产品在商店没有出售的情况
    result_df = melted_df.dropna(subset=['price'])
    
    # 重置索引并返回结果
    return result_df.reset_index(drop=True)
