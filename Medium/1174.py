import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # 首先找到每个顾客的首次订单
    # 按customer_id分组，找到每个顾客的最小order_date
    first_orders = delivery.groupby('customer_id')['order_date'].min().reset_index()
    
    # 合并首次订单信息到原始数据，找到对应的完整订单记录
    first_order_details = pd.merge(first_orders, delivery, on=['customer_id', 'order_date'], how='inner')
    
    # 判断是否为即时订单（下单日期与期望配送日期相同）
    first_order_details['is_immediate'] = (first_order_details['order_date'] == first_order_details['customer_pref_delivery_date']).astype(int)
    
    # 计算即时订单的比例
    immediate_count = first_order_details['is_immediate'].sum()
    total_count = len(first_order_details)
    immediate_percentage = round((immediate_count / total_count) * 100, 2) if total_count > 0 else 0.00
    
    # 创建结果DataFrame
    result = pd.DataFrame({'immediate_percentage': [immediate_percentage]})
    
    return result
