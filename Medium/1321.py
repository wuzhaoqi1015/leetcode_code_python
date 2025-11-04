import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    # 按访问日期分组，计算每日总消费金额
    daily_sales = customer.groupby('visited_on')['amount'].sum().reset_index()
    daily_sales = daily_sales.sort_values('visited_on').reset_index(drop=True)
    
    # 计算7天滚动总和和滚动平均值
    daily_sales['amount_7d'] = daily_sales['amount'].rolling(window=7, min_periods=7).sum()
    daily_sales['average_amount'] = daily_sales['amount'].rolling(window=7, min_periods=7).mean().round(2)
    
    # 过滤掉前6天（因为前6天无法构成完整的7天窗口）
    result = daily_sales[daily_sales['amount_7d'].notna()].copy()
    
    # 选择需要的列并重命名
    result = result[['visited_on', 'amount_7d', 'average_amount']]
    result.columns = ['visited_on', 'amount', 'average_amount']
    
    # 按访问日期升序排序
    result = result.sort_values('visited_on').reset_index(drop=True)
    
    return result
