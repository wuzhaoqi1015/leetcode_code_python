import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # 定义月份列表，确保顺序正确
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # 使用pivot_table进行数据透视，将月份作为列，收入作为值
    # 设置id为索引，month为列，revenue为值
    result = department.pivot_table(
        index='id',
        columns='month', 
        values='revenue',
        aggfunc='first'
    )
    
    # 重新索引列以确保所有月份都存在，即使某些月份没有数据
    result = result.reindex(columns=months)
    
    # 重命名列名，添加_Revenue后缀
    result.columns = [f"{month}_Revenue" for month in months]
    
    # 重置索引，将id从索引变回列
    result = result.reset_index()
    
    # 返回最终结果
    return result
