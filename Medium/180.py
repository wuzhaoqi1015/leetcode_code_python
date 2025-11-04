import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # 按id排序确保数据顺序正确
    logs = logs.sort_values('id')
    
    # 创建两个新的列，分别存储前一行和后一行的num值
    logs['prev_num'] = logs['num'].shift(1)
    logs['next_num'] = logs['num'].shift(-1)
    
    # 检查当前行的num是否等于前一行和后一行的num
    # 如果都相等，说明连续出现了三次
    consecutive_mask = (logs['num'] == logs['prev_num']) & (logs['num'] == logs['next_num'])
    
    # 筛选出满足条件的行，并提取num列
    result_nums = logs.loc[consecutive_mask, 'num']
    
    # 去重并创建结果DataFrame
    if not result_nums.empty:
        result_df = pd.DataFrame({'ConsecutiveNums': result_nums.unique()})
    else:
        result_df = pd.DataFrame(columns=['ConsecutiveNums'])
    
    return result_df
