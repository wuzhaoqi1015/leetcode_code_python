import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # 计算每个tiv_2015值出现的次数
    tiv_counts = insurance['tiv_2015'].value_counts()
    
    # 筛选出在2015年投保额至少与一个其他投保人相同的记录
    # 即tiv_2015值出现次数大于1的记录
    condition1 = insurance['tiv_2015'].isin(tiv_counts[tiv_counts > 1].index)
    
    # 计算每个地理位置(lat, lon)出现的次数
    location_counts = insurance.groupby(['lat', 'lon']).size()
    
    # 筛选出地理位置唯一的记录
    # 即(lat, lon)组合出现次数为1的记录
    condition2 = insurance.set_index(['lat', 'lon']).index.isin(location_counts[location_counts == 1].index)
    
    # 同时满足两个条件的记录
    valid_records = insurance[condition1 & condition2]
    
    # 计算满足条件的tiv_2016总和，并四舍五入到两位小数
    total_tiv_2016 = round(valid_records['tiv_2016'].sum(), 2)
    
    # 创建结果DataFrame
    result = pd.DataFrame({'tiv_2016': [total_tiv_2016]})
    
    return result
