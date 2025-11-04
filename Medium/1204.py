import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # 按turn列升序排序，确保按正确的上车顺序处理
    sorted_queue = queue.sort_values('turn').reset_index(drop=True)
    
    # 计算累积重量
    sorted_queue['cumulative_weight'] = sorted_queue['weight'].cumsum()
    
    # 找到累积重量不超过1000的最后一个人
    valid_passengers = sorted_queue[sorted_queue['cumulative_weight'] <= 1000]
    
    # 如果存在符合条件的乘客，取最后一个；否则返回空DataFrame
    if not valid_passengers.empty:
        last_valid = valid_passengers.iloc[[-1]]
        result = pd.DataFrame({'person_name': [last_valid['person_name'].iloc[0]]})
    else:
        result = pd.DataFrame({'person_name': []})
    
    return result
